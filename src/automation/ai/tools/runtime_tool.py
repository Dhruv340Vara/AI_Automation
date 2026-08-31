from __future__ import annotations

from automation.ai.tool import Tool
from automation.ai.tool_result import ToolResult
from automation.automation_runtime import AutomationRuntime


class RuntimeTool(Tool):
    """
    AI Tool for AutomationRuntime.
    """

    def __init__(
        self,
        runtime: AutomationRuntime | None = None,
    ):

        super().__init__(
            name="Runtime",
            description="Automation Runtime Tool",
        )

        self.runtime = (
            runtime
            or AutomationRuntime()
        )

    # ---------------------------- #

    def execute(
        self,
        operation: str,
        **kwargs,
    ) -> ToolResult:

        operation = operation.lower()

        try:

            if operation == "start":

                self.runtime.start()

                return ToolResult(
                    success=True,
                    message="Runtime started.",
                )

            if operation == "stop":

                self.runtime.stop()

                return ToolResult(
                    success=True,
                    message="Runtime stopped.",
                )

            if operation == "status":

                running = getattr(
                    self.runtime,
                    "running",
                    False,
                )

                return ToolResult(
                    success=True,
                    data=running,
                    message="Runtime status.",
                )

            if operation == "emit":

                event = kwargs.get(
                    "event",
                )

                result = self.runtime.emit_event(
                    event
                )

                return ToolResult(
                    success=result,
                    data=result,
                    message="Event emitted.",
                )

            return ToolResult(
                success=False,
                message=(
                    f"Unknown operation "
                    f"'{operation}'."
                ),
            )

        except Exception as error:

            return ToolResult(
                success=False,
                message=str(error),
            )
