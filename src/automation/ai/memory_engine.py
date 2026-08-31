from __future__ import annotations

from typing import Any

from automation.ai.memory_store import (
    MemoryStore,
)

from automation.ai.memory_search import (
    MemorySearch,
)


class MemoryEngine:
    """
    High-level interface for AI memory.
    """

    def __init__(
        self,
        store: MemoryStore | None = None,
    ):

        self.store = store or MemoryStore()

        self.searcher = MemorySearch()

    # -------------------------------- #

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

    # -------------------------------- #

    def __repr__(self):

        return "<MemoryEngine>"
