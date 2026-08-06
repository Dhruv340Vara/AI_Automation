from automation.ai.tool import (
    Tool,
)

from automation.ai.tool_registry import (
    ToolRegistry,
)


class DemoTool(
    Tool,
):

    def __init__(
        self,
        name,
    ):

        super().__init__(
            name=name,
        )

    def execute(
        self,
        **kwargs,
    ):

        return kwargs


registry = ToolRegistry()

tool1 = DemoTool(
    "File"
)

tool2 = DemoTool(
    "Memory"
)

registry.register(
    tool1
)

registry.register(
    tool2
)

print(registry)

print()

print(
    registry.count()
)

print()

print(
    registry.names()
)

print()

print(
    registry.exists(
        "File"
    )
)

print()

print(
    registry.get(
        "Memory"
    )
)

print()

registry.unregister(
    "File"
)

print(
    registry.names()
)

print()

registry.clear()

print(
    registry.count()
)
