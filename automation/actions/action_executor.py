from __future__ import annotations

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

        raise ValueError(
            f"Unsupported action type: {action_type}"
        )

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
