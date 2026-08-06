from automation.ai.tools.memory_tool import (
    MemoryTool,
)

tool = MemoryTool()

print(tool)

print()

tool.execute(
    operation="clear",
)

print("Remember")

print(
    tool.execute(
        operation="remember",
        key="user_name",
        value="Dhruv",
    )
)

print()

print("Recall")

print(
    tool.execute(
        operation="recall",
        key="user_name",
    )
)

print()

print("Search")

print(
    tool.execute(
        operation="search",
        keyword="dh",
    )
)

print()

print("Forget")

print(
    tool.execute(
        operation="forget",
        key="user_name",
    )
)

print()

print("Clear")

print(
    tool.execute(
        operation="clear",
    )
)
