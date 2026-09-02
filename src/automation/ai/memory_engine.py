from __future__ import annotations
import threading
import time
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
        """
        Store a conversation memory intelligently.

        - Ignores empty content
        - Calculates importance automatically
        - Classifies the memory
        - Ignores very low-value memories
        - Updates an existing similar memory
        - Creates a new memory only when no duplicate exists
        """

        if not content or not content.strip():
            return None

        # Calculate importance automatically
        if importance is None:
            importance = self.calculate_importance(
                content=content,
                role=role,
            )

        # Keep importance between 0 and 1
        importance = max(
            0.0,
            min(1.0, importance),
        )

        # Classify memory
        memory_type = self.classify_memory(content)

        # Ignore extremely low-value memories
        if importance < 0.15:
            return None

        # Find similar existing memory
        existing = self.find_similar_memory(
            content=content,
        )

        data = self.store.load()
        now = datetime.now().isoformat(timespec="seconds")

        # --------------------------------------------------
        # Existing memory found → UPDATE
        # --------------------------------------------------

        if existing:
            memory_id = existing["id"]

            existing["importance"] = max(
                float(existing.get("importance", 0.0)),
                importance,
            )

            existing["updated_at"] = now

            existing.setdefault(
                "last_accessed_at",
                now,
            )

            existing.setdefault(
                "access_count",
                0,
            )

            if metadata:
                existing.setdefault(
                    "metadata",
                    {},
                )
                existing["metadata"].update(metadata)

            data[memory_id] = existing
            self.store.save(data)

            return memory_id

        # --------------------------------------------------
        # No duplicate → CREATE new memory
        # --------------------------------------------------

        memory_id = str(uuid4())

        memory = {
            "id": memory_id,
            "type": "conversation",
            "memory_type": memory_type,
            "role": role,
            "content": content,
            "importance": importance,
            "created_at": now,
            "updated_at": now,
            "last_accessed_at": now,
            "access_count": 0,
            "metadata": metadata or {},
        }

        data[memory_id] = memory
        # Save new memory first.
        data[memory_id] = memory
        self.store.save(data)

        # Find memories that conflict with this new memory.
        conflicts = self.find_conflicting_memories(
            content=content,
            memory_type=memory_type,
        )

        # Mark conflicting memories as superseded.
        for conflict in conflicts:

            old_memory_id = conflict.get("id")

            if not old_memory_id:
                continue

            if old_memory_id == memory_id:
                continue

            self.supersede_memory(
                old_memory_id=old_memory_id,
                new_memory_id=memory_id,
            )

        return memory_id

    def search_conversation(
        self,
        query: str,
        limit: int = 5,
    ) -> list[dict]:
        """Search only active conversation memories."""

        if not query.strip():
            return []

        data = self.store.load()

        # Search conversation memories.
        memories = self.searcher.search_conversation(
            data,
            query,
        )

        # -------------------------------------------------
        # Filter superseded memories.
        # -------------------------------------------------

        active_memories = []

        for memory in memories:

            if not isinstance(memory, dict):
                continue

            # Default old memories to active for
            # backward compatibility.
            status = memory.get(
                "status",
                "active",
            )

            if status != "active":
                continue

            active_memories.append(memory)

        # -------------------------------------------------
        # Rank only active memories.
        # -------------------------------------------------

        ranked = self._rank_memories(
            active_memories
        )

        results = ranked[
            :max(0, limit)
        ]

        # -------------------------------------------------
        # Access tracking.
        # -------------------------------------------------

        now = datetime.now().isoformat(
            timespec="seconds"
        )

        for memory in results:

            memory_id = memory.get("id")

            if not memory_id:
                continue

            stored_memory = data.get(
                memory_id
            )

            if not isinstance(
                stored_memory,
                dict,
            ):
                continue

            stored_memory["access_count"] = int(
                stored_memory.get(
                    "access_count",
                    0,
                )
            ) + 1

            stored_memory["last_accessed_at"] = now

            data[memory_id] = stored_memory

        self.store.save(data)

        # Remove internal ranking fields.
        for memory in results:

            memory.pop(
                "_match_score",
                None,
            )

            memory.pop(
                "_final_score",
                None,
            )

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

    def _rank_memories(
        self,
        memories: list[dict],
    ) -> list[dict]:

        now = datetime.now()

        def score(memory):

            # -----------------------------------------
            # 1. Relevance
            # -----------------------------------------

            match_score = float(
                memory.get(
                    "_match_score",
                    0.0,
                )
            )

            # -----------------------------------------
            # 2. Importance
            # -----------------------------------------

            importance = float(
                memory.get(
                    "importance",
                    0.0,
                )
            )

            # -----------------------------------------
            # 3. Recency
            # -----------------------------------------

            created_at = memory.get(
                "created_at",
                "",
            )

            recency_score = 0.0

            try:
                created = datetime.fromisoformat(
                    created_at
                )

                age_days = max(
                    0.0,
                    (
                        now - created
                    ).total_seconds()
                    / 86400,
                )

                recency_score = (
                    1.0 / (1.0 + age_days)
                )

            except (
                ValueError,
                TypeError,
            ):
                recency_score = 0.0

            # -----------------------------------------
            # 4. Access Frequency
            # -----------------------------------------

            access_count = float(
                memory.get(
                    "access_count",
                    0,
                )
            )

            access_score = min(
                1.0,
                access_count / 10.0,
            )

            # -----------------------------------------
            # Final Ranking Score
            # -----------------------------------------

            final_score = (
                (match_score * 0.45)
                + (importance * 0.30)
                + (recency_score * 0.15)
                + (access_score * 0.10)
            )

            return final_score

        ranked = []

        for memory in memories:

            item = dict(memory)

            item["_final_score"] = score(
                memory
            )

            ranked.append(item)

        ranked.sort(
            key=lambda memory: memory[
                "_final_score"
            ],
            reverse=True,
        )

        return ranked

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

    def classify_memory(self, content: str) -> str:
        """
        Classify a conversation memory into a useful category.

        Returns:
            fact
            preference
            goal
            instruction
            conversation
        """

        text = content.lower().strip()

        if not text:
            return "conversation"

        # -----------------------------------------
        # Personal facts / identity
        # -----------------------------------------
        identity_patterns = [
            "my name is",
            "i live in",
            "my age is",
            "i was born",
        ]

        if any(pattern in text for pattern in identity_patterns):
            return "fact"

        # -----------------------------------------
        # Preferences
        # -----------------------------------------
        preference_patterns = [
            "i like",
            "i love",
            "i prefer",
            "i don't like",
            "i hate",
            "my favorite",
        ]

        if any(pattern in text for pattern in preference_patterns):
            return "preference"

        # -----------------------------------------
        # Goals / projects
        # -----------------------------------------
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
            return "goal"

        # -----------------------------------------
        # Instructions / permanent preferences
        # -----------------------------------------
        instruction_patterns = [
            "remember that",
            "don't forget",
            "always",
            "never",
            "from now on",
            "going forward",
        ]

        if any(pattern in text for pattern in instruction_patterns):
            return "instruction"

        # -----------------------------------------
        # Normal conversation
        # -----------------------------------------
        return "conversation"

    def find_similar_memory(self,content: str,memory_type: str | None = None,) -> dict | None:
        """
        Find an existing conversation memory
        that is highly similar to the given content.
        """

        data = self.store.load()

        new_words = {
            word.strip(".,!?;:")
            for word in content.lower().split()
            if word.strip(".,!?;:")
        }

        if not new_words:
            return None

        best_memory = None
        best_score = 0.0

        for memory in data.values():

            if not isinstance(memory, dict):
                continue

            if memory.get("type") != "conversation":
                continue

            old_content = str(
                memory.get("content", "")
            ).lower()

            old_words = {
                word.strip(".,!?;:")
                for word in old_content.split()
                if word.strip(".,!?;:")
            }

            if not old_words:
                continue

            intersection = new_words & old_words
            union = new_words | old_words

            score = len(intersection) / len(union)

            if score > best_score:
                best_score = score
                best_memory = memory

        if best_score >= 0.75:
            return best_memory

        return None

    def cleanup_memories(
        self,
        min_importance: float = 0.30,
        max_age_days: int = 30,
    ) -> int:
        """
        Remove old, unused, low-importance conversation memories.

        Safe cleanup rules:
        - Only conversation memories are eligible.
        - Important memories are protected.
        - Facts, preferences, goals and instructions are protected.
        - Accessed memories are protected.
        - Recent memories are protected.

        Returns:
            Number of deleted memories.
        """

        data = self.store.load()

        now = datetime.now()
        keys_to_remove = []
        scanned_count = 0

        protected_types = {
            "fact",
            "preference",
            "goal",
            "instruction",
        }

        for key, memory in data.items():

            if not isinstance(memory, dict):
                continue

            # Don't process system logs.
            if memory.get("type") != "conversation":
                continue

            scanned_count += 1

            memory_type = memory.get(
                "memory_type",
                "conversation",
            )

            # Protect important memory categories.
            if memory_type in protected_types:
                continue

            importance = float(
                memory.get("importance", 0.0)
            )

            # Protect important memories.
            if importance >= 0.75:
                continue

            # Only clean low-importance memories.
            if importance >= min_importance:
                continue

            access_count = int(
                memory.get("access_count", 0)
            )

            # Never delete accessed memories.
            if access_count > 0:
                continue

            created_at = memory.get("created_at", "")

            try:
                created = datetime.fromisoformat(
                    created_at
                )
            except (ValueError, TypeError):
                # Invalid date -> protect memory.
                continue

            age_days = (
                now - created
            ).total_seconds() / 86400

            # Protect recent memories.
            if age_days < max_age_days:
                continue

            keys_to_remove.append(key)

        # Delete selected memories.
        for key in keys_to_remove:
            del data[key]

        deleted_count = len(keys_to_remove)

        # Save memory changes.
        self.store.save(data)

        # Write cleanup log.
        self._log_cleanup(
            deleted_count=deleted_count,
            scanned_count=scanned_count,
        )

        return deleted_count

    def _log_cleanup(
        self,
        deleted_count: int,
        scanned_count: int,
        max_logs: int = 50,
    ) -> None:
        """Store cleanup activity and keep only recent logs."""

        data = self.store.load()

        now = datetime.now().isoformat(
            timespec="seconds"
        )

        # UUID guarantees that every log has
        # a unique key, even when multiple logs
        # are created within the same second.
        log_id = f"cleanup_log_{uuid4()}"

        data[log_id] = {
            "type": "system_log",
            "log_type": "memory_cleanup",
            "created_at": now,
            "deleted_count": deleted_count,
            "scanned_count": scanned_count,
        }

        # Collect existing cleanup logs.
        logs = []

        for key, memory in data.items():

            if not isinstance(memory, dict):
                continue

            if memory.get("type") != "system_log":
                continue

            if memory.get("log_type") != "memory_cleanup":
                continue

            logs.append(
                (
                    key,
                    memory.get("created_at", ""),
                )
            )

        # Newest logs first.
        logs.sort(
            key=lambda item: item[1],
            reverse=True,
        )

        # Keep only the newest max_logs entries.
        for key, _ in logs[max_logs:]:
            data.pop(key, None)

        self.store.save(data)

    def cleanup_logs(
        self,
        limit: int = 20,
    ) -> list[dict]:
        """Return recent memory cleanup logs."""

        data = self.store.load()

        logs = []

        for memory in data.values():

            if not isinstance(memory, dict):
                continue

            if memory.get("type") != "system_log":
                continue

            if memory.get("log_type") != "memory_cleanup":
                continue

            logs.append(dict(memory))

        logs.sort(
            key=lambda item: item.get(
                "created_at",
                "",
            ),
            reverse=True,
        )

        return logs[:max(0, limit)]

    def start_auto_cleanup(
        self,
        interval_hours: int = 24,
        min_importance: float = 0.30,
        max_age_days: int = 30,
    ) -> None:
        """
        Start automatic background memory cleanup.

        Cleanup runs once every interval_hours.
        """

        if interval_hours <= 0:
            raise ValueError(
                "interval_hours must be greater than 0"
            )

        # Don't start multiple cleanup threads.
        if getattr(
            self,
            "_cleanup_thread",
            None,
        ) is not None:

            if self._cleanup_thread.is_alive():
                return

        self._cleanup_stop_event = threading.Event()

        def cleanup_loop():

            while not self._cleanup_stop_event.is_set():

                try:
                    self.cleanup_memories(
                        min_importance=min_importance,
                        max_age_days=max_age_days,
                    )

                except Exception as error:
                    print(
                        f"[MemoryCleanup] Error: {error}"
                    )

                # Wait until next cleanup.
                self._cleanup_stop_event.wait(
                    interval_hours * 3600
                )

        self._cleanup_thread = threading.Thread(
            target=cleanup_loop,
            name="MemoryCleanupThread",
            daemon=True,
        )

        self._cleanup_thread.start()

    def stop_auto_cleanup(self) -> None:
        """Stop automatic memory cleanup."""

        stop_event = getattr(
            self,
            "_cleanup_stop_event",
            None,
        )

        if stop_event is not None:
            stop_event.set()

        thread = getattr(
            self,
            "_cleanup_thread",
            None,
        )

        if thread is not None and thread.is_alive():
            thread.join(timeout=2)

        self._cleanup_thread = None

    def cleanup_statistics(self) -> dict:
        """Return cleanup statistics."""

        logs = self.cleanup_logs(limit=50)

        total_runs = len(logs)

        total_scanned = sum(
            int(log.get("scanned_count", 0))
            for log in logs
        )

        total_deleted = sum(
            int(log.get("deleted_count", 0))
            for log in logs
        )

        return {
            "total_runs": total_runs,
            "total_scanned": total_scanned,
            "total_deleted": total_deleted,
        }

    def find_conflicting_memories(
        self,
        content: str,
        memory_type: str | None = None,
    ) -> list[dict]:
        """
        Find active memories that may conflict with new content.
        """

        if not content or not content.strip():
            return []

        data = self.store.load()

        new_text = content.lower().strip()

        if memory_type is None:
            memory_type = self.classify_memory(content)

        # Only these memory categories need conflict detection.
        conflict_types = {
            "fact",
            "preference",
            "goal",
            "instruction",
        }

        if memory_type not in conflict_types:
            return []

        conflicts = []

        for memory in data.values():

            if not isinstance(memory, dict):
                continue

            if memory.get("type") != "conversation":
                continue

            # Ignore already superseded memories.
            if memory.get("status", "active") != "active":
                continue

            existing_type = memory.get(
                "memory_type",
                "conversation",
            )

            # Conflict is only checked within
            # the same memory category.
            if existing_type != memory_type:
                continue

            existing_content = str(
                memory.get("content", "")
            ).lower().strip()

            if not existing_content:
                continue

            # Don't compare a memory with itself.
            if existing_content == new_text:
                continue

            # Basic conflict detection.
            #
            # We currently identify potential conflicts
            # by category and related keywords.
            new_words = {
                word.strip(".,!?;:")
                for word in new_text.split()
                if word.strip(".,!?;:")
            }

            old_words = {
                word.strip(".,!?;:")
                for word in existing_content.split()
                if word.strip(".,!?;:")
            }

            if not new_words or not old_words:
                continue

            overlap = new_words & old_words

            similarity = (
                len(overlap)
                / len(new_words | old_words)
            )

            # A reasonably related memory is a
            # potential conflict candidate.
            if similarity >= 0.20:
                result = dict(memory)
                result["_conflict_score"] = similarity
                conflicts.append(result)

        conflicts.sort(
            key=lambda memory: memory.get(
                "_conflict_score",
                0.0,
            ),
            reverse=True,
        )

        return conflicts

    def supersede_memory(
        self,
        old_memory_id: str,
        new_memory_id: str,
    ) -> bool:
        """
        Mark an existing memory as superseded by a newer memory.

        The old memory is preserved for history.
        """

        data = self.store.load()

        old_memory = data.get(old_memory_id)

        if not isinstance(old_memory, dict):
            return False

        # Don't supersede an already superseded memory.
        if old_memory.get("status") == "superseded":
            return False

        now = datetime.now().isoformat(
            timespec="seconds"
        )

        old_memory["status"] = "superseded"
        old_memory["superseded_by"] = new_memory_id
        old_memory["superseded_at"] = now
        old_memory["updated_at"] = now

        data[old_memory_id] = old_memory

        self.store.save(data)

        return True