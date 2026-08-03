from __future__ import annotations
from automation.security.command_validator import (
    CommandValidator
)
from typing import Any
import subprocess
from automation.automation_types import Automation


class ActionExecutor:
    def __init__(self):
        self.validator = CommandValidator()

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

        if action_type == "shell_command":
            return self._shell_command(action)

        raise ValueError(
            f"Unsupported action type: {action_type}"
        )

    def _shell_command(
        self,
        action: dict[str, Any]
    ) -> bool:
        self.validator.validate(
            command
        )
        command = action.get("command")

        if not command:
            raise ValueError(
                "Missing shell command."
            )

        shell = action.get(
            "shell",
            True
        )

        capture_output = action.get(
            "capture_output",
            True
        )

        text = action.get(
            "text",
            True
        )

        result = subprocess.run(
            command,
            shell=shell,
            capture_output=capture_output,
            text=text,
        )

        if capture_output:

            if result.stdout:
                print(result.stdout.strip())

            if result.stderr:
                print(result.stderr.strip())

        return result.returncode == 0

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
