from automation.ai.tools.shell_tool import (
    ShellTool,
)

tool = ShellTool()

print(tool)

print()

print("PWD")

result = tool.execute(
    command="pwd",
)

print(result)

print(result.data)

print()

print("LIST")

result = tool.execute(
    command="ls",
)

print(result)

print(result.data)

print()

print("INVALID")

result = tool.execute(
    command="unknown_command",
)

print(result)

print(result.data)

