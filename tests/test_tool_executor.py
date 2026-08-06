from automation.ai.tool import (
    Tool,
)

from automation.ai.tool_registry import (
    ToolRegistry,
)

from automation.ai.tool_executor import (
    ToolExecutor,
)

from automation.ai.tool_result import (
    ToolResult,
)


class DemoTool(
    Tool,
):

    def __init__(self):

        super().__init__(

            name="Demo",

            description="Demo Tool",

        )

    def execute(
        self,
        **kwargs,
    ):

        return ToolResult(

            success=True,

            data=kwargs,

            message="Demo executed",

        )


registry = ToolRegistry()

registry.register(
    DemoTool()
)

executor = ToolExecutor(
    registry
)

print(executor)

print()

result = executor.execute(

    "Demo",

    name="Dhruv",

    age=21,

)

print(result)

print()

print(result.to_dict())

print()

print(executor.execution_count())

print()

missing = executor.execute(
    "Unknown"
)

print(missing)

print()

print(missing.message)

print()

tool = registry.get(
    "Demo"
)

tool.disable()

disabled = executor.execute(
    "Demo"
)

print(disabled)

print()

print(disabled.message)
