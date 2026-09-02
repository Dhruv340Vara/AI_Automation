from __future__ import annotations

from datetime import datetime
from typing import Any
from uuid import uuid4
from automation.ai.memory_store import (
    MemoryStore,
)

from automation.ai.memory_search import (
    MemorySearch,
)


class MemoryEngine:
    """
    High-level interface for AI memory.

    Supports:
    - Key/value memory
    - Conversation memory
    - Memory metadata
    - Memory types
    - Importance
    - Recent memory retrieval
    - Conversation search
    - Type-based memory retrieval
    """

    def __init__(
        self,
        store: MemoryStore | None = None,
    ):

        self.store = store or MemoryStore()

        self.searcher = MemorySearch()

    # ==========================================================
    # BASIC KEY / VALUE MEMORY
    # ==========================================================

    def get(
        self,
        key: str,
        default=None,
    ):

        data = self.store.load()

        return self.searcher.find(
            data,
            key,
            default,
        )

    # -------------------------------- #

    def set(
        self,
        key: str,
        value: Any,
    ):

        data = self.store.load()

        data[key] = value

        self.store.save(
            data
        )

    # -------------------------------- #

    def remove(
        self,
        key: str,
    ):

        data = self.store.load()

        if key in data:

            del data[key]

            self.store.save(
                data
            )

            return True

        return False

    # -------------------------------- #

    def exists(
        self,
        key: str,
    ):

        data = self.store.load()

        return self.searcher.exists(
            data,
            key,
        )

    # -------------------------------- #

    def search(
        self,
        keyword: str,
    ):

        data = self.store.load()

        return self.searcher.search(
            data,
            keyword,
        )

    # -------------------------------- #

    def keys(self):

        return self.searcher.keys(
            self.store.load()
        )

    # -------------------------------- #

    def values(self):

        return self.searcher.values(
            self.store.load()
        )

    # -------------------------------- #

    def clear(self):

        self.store.clear()

    # ==========================================================
    # CONVERSATION MEMORY
    # ==========================================================

    def remember_conversation(
    self,
    role: str,
    content: str,
    importance: float | None = None,
    metadata=None,
):
        if importance is None:
            importance = self.calculate_importance(
                content=content,
                role=role,
            )

        importance = max(
            0.0,
            min(1.0, importance),
        )

        memory_id = str(uuid4())

        memory = {
            "id": memory_id,
            "type": "conversation",
            "role": role,
            "content": content,
            "importance": importance,
            "created_at": datetime.now().isoformat(
                timespec="seconds"
            ),
            "metadata": metadata or {},
        }

        self.set(memory_id, memory)

        return memory_id

    def search_conversation(self, query: str, limit: int = 5) -> list[dict]:
        if not query.strip():
            return []

        data = self.store.load()

        memories = self.searcher.search_conversation(
            data,
            query,
        )

        ranked = self._rank_memories(memories)

        results = ranked[:max(0, limit)]

        for memory in results:
            memory.pop("_match_score", None)
            memory.pop("_final_score", None)

        return results

    def recent_memories(
        self,
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        """
        Return the most recently created memories.
        """

        data = self.store.load()

        memories = [

            value

            for value in data.values()

            if isinstance(value, dict)

            and "id" in value

            and "created_at" in value

        ]

        memories.sort(
            key=lambda item: item.get(
                "created_at",
                "",
            ),
            reverse=True,
        )

        return memories[
            :max(0, limit)
        ]

    # -------------------------------- #

    def memories_by_type(
        self,
        memory_type: str,
        limit: int | None = None,
    ) -> list[dict[str, Any]]:
        """
        Return memories belonging to a specific type.
        """

        data = self.store.load()

        memories = [

            value

            for value in data.values()

            if isinstance(value, dict)

            and value.get("type")
            == memory_type

        ]

        memories.sort(
            key=lambda item: (
                item.get(
                    "importance",
                    0.0,
                ),
                item.get(
                    "created_at",
                    "",
                ),
            ),
            reverse=True,
        )

        if limit is not None:

            return memories[
                :max(0, limit)
            ]

        return memories

    # -------------------------------- #

    def forget_memory(
        self,
        memory_id: str,
    ) -> bool:
        """
        Delete a specific memory by ID.
        """

        data = self.store.load()

        if memory_id not in data:

            return False

        del data[memory_id]

        self.store.save(
            data
        )

        return True

    # -------------------------------- #

    def clear_memory_type(
        self,
        memory_type: str,
    ) -> int:
        """
        Delete all memories of a specific type.

        Returns:
            Number of deleted memories.
        """

        data = self.store.load()

        keys_to_remove = [

            key

            for key, value in data.items()

            if isinstance(value, dict)

            and value.get("type")
            == memory_type

        ]

        for key in keys_to_remove:

            del data[key]

        self.store.save(
            data
        )

        return len(
            keys_to_remove
        )

    # ==========================================================
    # INTERNAL HELPERS
    # ==========================================================

    def _rank_memories(self, memories: list[dict]) -> list[dict]:
        from datetime import datetime

        now = datetime.now()

        def score(memory):
            match_score = float(
                memory.get("_match_score", 0.0)
            )

            importance = float(
                memory.get("importance", 0.0)
            )

            created_at = memory.get("created_at", "")

            recency_score = 0.0

            try:
                created = datetime.fromisoformat(created_at)

                age_days = max(
                    0.0,
                    (now - created).total_seconds() / 86400,
                )

                # Recent memory gets higher score.
                recency_score = 1.0 / (1.0 + age_days)

            except (ValueError, TypeError):
                recency_score = 0.0

            # Final ranking score
            final_score = (
                (match_score * 0.50)
                + (importance * 0.35)
                + (recency_score * 0.15)
            )

            return final_score

        ranked = []

        for memory in memories:
            item = dict(memory)

            item["_final_score"] = score(memory)

            ranked.append(item)

        ranked.sort(
            key=lambda memory: memory["_final_score"],
            reverse=True,
        )

        return ranked

    # ==========================================================

    def __repr__(self):

        return "<MemoryEngine>"

    def calculate_importance(self, content: str, role: str = "user") -> float:
        """
        Calculate how important a conversation message is for long-term memory.
        Returns a value between 0.0 and 1.0.
        """

        text = content.lower().strip()

        if not text:
            return 0.0

        # Very short conversational messages
        low_value_phrases = {
            "ok",
            "okay",
            "thanks",
            "thank you",
            "hi",
            "hello",
            "hey",
            "bye",
            "goodbye",
            "yes",
            "no",
            "sure",
        }

        if text in low_value_phrases:
            return 0.05

        # Strong personal facts / identity
        identity_patterns = [
            "my name is",
            "i am ",
            "i'm ",
            "i live in",
            "my age is",
            "i was born",
        ]

        if any(pattern in text for pattern in identity_patterns):
            return 0.95

        # Preferences
        preference_patterns = [
            "i like",
            "i love",
            "i prefer",
            "i don't like",
            "i hate",
            "my favorite",
            "i prefer",
        ]

        if any(pattern in text for pattern in preference_patterns):
            return 0.85

        # Long-term goals / projects
        goal_patterns = [
            "my goal is",
            "i want to",
            "i am working on",
            "i'm working on",
            "my project",
            "i plan to",
            "i am building",
            "i'm building",
        ]

        if any(pattern in text for pattern in goal_patterns):
            return 0.80

        # Important instructions / decisions
        instruction_patterns = [
            "remember that",
            "don't forget",
            "always",
            "never",
            "from now on",
            "going forward",
        ]

        if any(pattern in text for pattern in instruction_patterns):
            return 0.90

        # Assistant messages are generally less important than user facts
        if role == "assistant":
            return 0.25

        # Default user message
        return 0.50