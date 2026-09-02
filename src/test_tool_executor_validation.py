from automation.ai.tool_registry import ToolRegistry
from automation.ai.tool_executor import ToolExecutor
from automation.ai.tools.shell_tool import ShellTool


def main():
    print("=== Tool Executor Argument Validation Test ===")

    registry = ToolRegistry()

    shell = ShellTool()
    registry.register(shell)

    executor = ToolExecutor(registry)

    # 1. Valid arguments
    result = executor.execute(
        "Shell",
        command="pwd",
    )

    assert result.success
    print("[PASS] Valid arguments executed")

    # 2. Missing required argument
    result = executor.execute(
        "Shell",
    )

    assert not result.success
    assert "Missing required argument" in result.message

    print("[PASS] Missing argument rejected")

    # 3. Wrong argument type
    result = executor.execute(
        "Shell",
        command=123,
    )

    assert not result.success
    assert "must be a string" in result.message

    print("[PASS] Wrong argument type rejected")

    # 4. Unknown argument
    result = executor.execute(
        "Shell",
        command="pwd",
        unknown="value",
    )

    assert not result.success
    assert "Unknown argument" in result.message

    print("[PASS] Unknown argument rejected")

    print("\nTOOL EXECUTOR VALIDATION TEST PASSED")


if __name__ == "__main__":
    main()
