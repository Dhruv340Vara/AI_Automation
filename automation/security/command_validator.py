from __future__ import annotations

import shlex

from automation.security.security_policy import (
    SAFE_COMMANDS,
)


class CommandValidator:

    def validate(
        self,
        command: str
    ) -> bool:

        if not command.strip():
            raise ValueError(
                "Empty command."
            )

        tokens = shlex.split(
            command
        )

        executable = tokens[0]

        if executable not in SAFE_COMMANDS:

            raise PermissionError(
                f"Blocked command: {executable}"
            )

        return True
