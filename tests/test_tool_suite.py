from automation.ai.ai_brain import (
    AIBrain,
)

from automation.ai.tools.memory_tool import (
    MemoryTool,
)

from automation.ai.tools.runtime_tool import (
    RuntimeTool,
)

from automation.ai.tools.shell_tool import (
    ShellTool,
)

print("=" * 60)
print("             TOOL TEST SUITE")
print("=" * 60)

brain = AIBrain()

print()
print("Registering Tools...")

brain.register_tool(
    MemoryTool()
)

brain.register_tool(
    RuntimeTool()
)

brain.register_tool(
    ShellTool()
)

assert (
    len(
        brain.available_tools()
    )
    == 3
)

print("PASS")

print()
print("Memory Tool...")

result = brain.execute_tool(

    "Memory",

    operation="clear",

)

assert result.success

result = brain.execute_tool(

    "Memory",

    operation="remember",

    key="user",

    value="Dhruv",

)

assert result.success

result = brain.execute_tool(

    "Memory",

    operation="recall",

    key="user",

)

assert result.success

assert (
    result.data
    == "Dhruv"
)

print("PASS")

print()
print("Runtime Tool...")

result = brain.execute_tool(

    "Runtime",

    operation="start",

)

assert result.success

result = brain.execute_tool(

    "Runtime",

    operation="status",

)

assert result.success

result = brain.execute_tool(

    "Runtime",

    operation="stop",

)

assert result.success

print("PASS")

print()
print("Shell Tool...")

result = brain.execute_tool(

    "Shell",

    command="pwd",

)

assert result.success

assert (
    result.data[
        "returncode"
    ]
    == 0
)

print("PASS")

print()
print("Unknown Tool...")

result = brain.execute_tool(

    "Unknown",

)

assert not result.success

print("PASS")

print()
print("Registered Tools:")

print(
    brain.available_tools()
)

print()

print("=" * 60)
print("ALL TOOL TESTS PASSED")
print("=" * 60)
