from __future__ import annotations

from automation.ai.tool import (
    Tool,
)

from automation.ai.tool_result import (
    ToolResult,
)

from automation.ai.memory_engine import (
    MemoryEngine,
)


class MemoryTool(Tool):
    """
    AI Tool for interacting with MemoryEngine.
    """

    def __init__(
        self,
        memory: MemoryEngine | None = None,
    ):

        super().__init__(
            name="Memory",
            description="Memory Tool",
        )

        self.memory = (
            memory
            or MemoryEngine()
        )

    # ---------------------------- #

    def execute(
        self,
        operation: str,
        **kwargs,
    ) -> ToolResult:

        operation = operation.lower()

        try:

            if operation == "remember":

                self.memory.set(
                    kwargs["key"],
                    kwargs["value"],
                )

                return ToolResult(
                    success=True,
                    message="Memory saved.",
                )

            if operation == "recall":

                value = self.memory.get(
                    kwargs["key"],
                )

                return ToolResult(
                    success=True,
                    data=value,
                    message="Memory loaded.",
                )

            if operation == "forget":

                removed = self.memory.remove(
                    kwargs["key"],
                )

                return ToolResult(
                    success=removed,
                    data=removed,
                    message="Memory removed.",
                )

            if operation == "search":

                result = self.memory.search(
                    kwargs["keyword"],
                )

                return ToolResult(
                    success=True,
                    data=result,
                    message="Search completed.",
                )

            if operation == "clear":

                self.memory.clear()

                return ToolResult(
                    success=True,
                    message="Memory cleared.",
                )

            return ToolResult(
                success=False,
                message=f"Unknown operation '{operation}'.",
            )

        except Exception as error:

            return ToolResult(
                success=False,
                message=str(error),
            )