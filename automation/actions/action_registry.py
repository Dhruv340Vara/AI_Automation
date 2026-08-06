from __future__ import annotations

from typing import Callable


class ActionRegistry:

    def __init__(self):

        self._actions: dict[str, Callable] = {}

    def register(
        self,
        action_type: str,
        handler: Callable
    ):

        self._actions[action_type] = handler

    def unregister(
        self,
        action_type: str
    ):

        self._actions.pop(
            action_type,
            None
        )

    def get(
        self,
        action_type: str
    ):

        return self._actions.get(
            action_type
        )

    def exists(
        self,
        action_type: str
    ) -> bool:

        return action_type in self._actions

    def execute(
        self,
        action_type: str,
        action: dict
    ):

        handler = self.get(
            action_type
        )

        if handler is None:
            raise ValueError(
                f"Unknown action: {action_type}"
            )

        return handler(action)

    def clear(self):

        self._actions.clear()

    def count(self):

        return len(
            self._actions
        )

    def __len__(self):

        return len(
            self._actions
        )
