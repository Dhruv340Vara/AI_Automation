from automation.ai.ai_brain import AIBrain
from automation.ai.tool_call import ToolCall
from automation.ai.tools.shell_tool import ShellTool


def main():
    print("=== Tool Call Execution Test ===")

    brain = AIBrain()

    shell = ShellTool()
    brain.register_tool(shell)

    tool_call = ToolCall(
        tool="Shell",
        arguments={
            "command": "pwd",
        },
    )

    print("Tool Call:")
    print(tool_call.to_dict())

    result = brain.execute_tool_call(tool_call)

    print("\nTool Result:")
    print(result)

    assert result.success
    assert result.data is not None

    print("\n[PASS] ToolCall executed")
    print("[PASS] ToolResult returned")
    print("[PASS] Shell command executed successfully")

    print("\nTOOL CALL EXECUTION TEST PASSED")


if __name__ == "__main__":
    main()
