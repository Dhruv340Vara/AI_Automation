from __future__ import annotations

from typing import Callable


class RuntimeCallbacks:

    def __init__(self):

        self._callbacks: dict[str, Callable] = {}

    def register(
        self,
        name: str,
        callback: Callable
    ):

        self._callbacks[name] = callback

    def unregister(
        self,
        name: str
    ):

        self._callbacks.pop(name, None)

    def get(
        self,
        name: str
    ):

        return self._callbacks.get(name)

    def exists(
        self,
        name: str
    ) -> bool:

        return name in self._callbacks

    def clear(self):

        self._callbacks.clear()

    def count(self):

        return len(self._callbacks)

    def __len__(self):

        return len(self._callbacks)
