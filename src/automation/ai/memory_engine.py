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
        importance: float = 0.5,
        metadata: dict[str, Any] | None = None,
    ) -> str:
        """
        Store a conversation message in long-term memory.

        Returns:
            Memory ID
        """

        data = self.store.load()

        memory_id = str(uuid4())

        memory = {
            "id": memory_id,
            "type": "conversation",
            "role": role,
            "content": content,
            "importance": max(
                0.0,
                min(1.0, importance),
            ),
            "created_at": datetime.now().isoformat(
                timespec="seconds"
            ),
            "metadata": metadata or {},
        }

        data[memory_id] = memory

        self.store.save(
            data
        )

        return memory_id

    # -------------------------------- #

    def search_conversation(
        self,
        query: str,
        limit: int = 5,
    ) -> list[dict[str, Any]]:
        """
        Search conversation memories.

        Returns the most relevant matching memories.
        """

        data = self.store.load()

        results = self.searcher.search_conversation(
            data,
            query,
        )

        results = self._rank_memories(
            results
        )

        return results[:max(0, limit)]

    # -------------------------------- #

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

    def _rank_memories(
        self,
        memories: list[dict[str, Any]],
    ) -> list[dict[str, Any]]:
        """
        Rank memories by importance and recency.
        """

        return sorted(

            memories,

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

    # ==========================================================

    def __repr__(self):

        return "<MemoryEngine>"