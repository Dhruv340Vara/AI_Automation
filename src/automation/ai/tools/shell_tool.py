from __future__ import annotations

import subprocess

from automation.ai.tool import Tool
from automation.ai.tool_result import ToolResult


class ShellTool(Tool):
    """
    AI Tool for executing shell commands.
    """

    def __init__(self):

        super().__init__(
            name="Shell",
            description="Shell Command Tool",
        )

    # ---------------------------- #

    def argument_schema(self) -> dict:
        return {
            "type": "object",
            "properties": {
                "command": {
                    "type": "string",
                    "description": "Shell command to execute.",
                },
                "cwd": {
                    "type": "string",
                    "description": "Optional working directory.",
                },
                "timeout": {
                    "type": "integer",
                    "description": "Maximum execution time in seconds.",
                },
            },
            "required": [
                "command",
            ],
        }

    def execute(
        self,
        command: str,
        cwd: str | None = None,
        timeout: int = 30,
        **kwargs,
    ) -> ToolResult:

        try:

            result = subprocess.run(

                command,

                shell=True,

                cwd=cwd,

                timeout=timeout,

                capture_output=True,

                text=True,

            )

            return ToolResult(

                success=(
                    result.returncode == 0
                ),

                data={

                    "stdout": result.stdout,

                    "stderr": result.stderr,

                    "returncode": result.returncode,

                },

                message="Command executed.",

            )

        except Exception as error:

            return ToolResult(

                success=False,

                message=str(error),

            )

