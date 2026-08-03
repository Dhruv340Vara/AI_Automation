from __future__ import annotations
from typing import Any, Callable
from typing import Any

from automation.automation_types import Automation


class ActionExecutor:

    def execute(
        self,
        automation: Automation
    ) -> bool:

        action = automation.action

        action_type = action.get("type")

        if action_type == "print":
            return self._print(action)

        if action_type == "python_function":
            return self._python_function(action)

        raise ValueError(
            f"Unsupported action type: {action_type}"
        )

    def _python_function(
        self,
        action: dict[str, Any]
    ) -> bool:

        function = action.get("function")

        if function is None:
            raise ValueError(
                "Missing function."
            )

        if not callable(function):
            raise TypeError(
                "function must be callable."
            )

        args = action.get(
            "args",
            []
        )

        kwargs = action.get(
            "kwargs",
            {}
        )

        function(
            *args,
            **kwargs
        )

        return True

    def _print(
        self,
        action: dict[str, Any]
    ) -> bool:

        message = action.get(
            "message",
            ""
        )

        print(message)

        return True
