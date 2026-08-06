from __future__ import annotations

from automation.ai.tool_registry import (
    ToolRegistry,
)

from automation.ai.tool_result import (
    ToolResult,
)


class ToolExecutor:
    """
    Executes tools registered in
    the ToolRegistry.
    """

    def __init__(
        self,
        registry: ToolRegistry | None = None,
    ):

        self.registry = (
            registry
            or ToolRegistry()
        )

        self.executed = 0

    # -------------------------------- #

    def execute(
        self,
        tool_name: str,
        **kwargs,
    ) -> ToolResult:

        tool = self.registry.get(
            tool_name
        )

        if tool is None:

            return ToolResult(

                success=False,

                message=(
                    f"Tool '{tool_name}' "
                    "not found."
                ),

            )

        if not tool.is_enabled():

            return ToolResult(

                success=False,

                message=(
                    f"Tool '{tool_name}' "
                    "is disabled."
                ),

            )

        result = tool.execute(
            **kwargs
        )

        self.executed += 1

        if isinstance(
            result,
            ToolResult,
        ):
            return result

        return ToolResult(

            success=True,

            data=result,

            message="Completed",

        )

    # -------------------------------- #

    def execution_count(
        self,
    ):

        return self.executed

    # -------------------------------- #

    def reset(
        self,
    ):

        self.executed = 0

    # -------------------------------- #

    def __repr__(
        self,
    ):

        return (
            "<ToolExecutor "
            f"executed={self.executed}>"
        )
