from __future__ import annotations

import subprocess

from automation.security.command_validator import (
    CommandValidator
)

_validator = CommandValidator()


def execute(
    action: dict
):

    command = action["command"]

    _validator.validate(
        command
    )

    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )

    if result.stdout:
        print(
            result.stdout.strip()
        )

    return (
        result.returncode == 0
    )
