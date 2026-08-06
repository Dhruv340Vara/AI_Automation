from automation.ai.tools.runtime_tool import (
    RuntimeTool,
)

tool = RuntimeTool()

print(tool)

print()

print("Start")

print(
    tool.execute(
        operation="start",
    )
)

print()

print("Status")

print(
    tool.execute(
        operation="status",
    )
)

print()

print("Stop")

print(
    tool.execute(
        operation="stop",
    )
)

print()

print("Status")

print(
    tool.execute(
        operation="status",
    )
)
