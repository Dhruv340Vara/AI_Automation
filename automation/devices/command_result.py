"""
command_result.py

Result returned by CommandRunner.
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import datetime


@dataclass
class CommandResult:

    success: bool

    stdout: str = ""

    stderr: str = ""

    returncode: int = 0

    execution_time: float = 0.0

    created_at: str = field(

        default_factory=lambda:

        datetime.now().isoformat(

            timespec="seconds"

        )

    )

    # ---------------------------- #

    def to_dict(self):

        return {

            "success": self.success,

            "stdout": self.stdout,

            "stderr": self.stderr,

            "returncode": self.returncode,

            "execution_time": self.execution_time,

            "created_at": self.created_at,

        }

    # ---------------------------- #

    @property
    def failed(self):

        return not self.success

    # ---------------------------- #

    def __bool__(self):

        return self.success

    # ---------------------------- #

    def __repr__(self):

        state = (

            "success"

            if self.success

            else "failed"

        )

        return (

            f"<CommandResult {state}>"

        )
