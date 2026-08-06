from automation.ai.ai_brain import (
    AIBrain,
)

from automation.ai.tools.memory_tool import (
    MemoryTool,
)

from automation.ai.tools.shell_tool import (
    ShellTool,
)

brain = AIBrain()

brain.register_tool(
    MemoryTool()
)

brain.register_tool(
    ShellTool()
)

print(brain)

print()

print("Available")

print(
    brain.available_tools()
)

print()

print("Remember")

print(

    brain.execute_tool(

        "Memory",

        operation="remember",

        key="user",

        value="Dhruv",

    )

)

print()

print("Recall")

print(

    brain.execute_tool(

        "Memory",

        operation="recall",

        key="user",

    )

)

print()

print("Shell")

print(

    brain.execute_tool(

        "Shell",

        command="pwd",

    )

)
