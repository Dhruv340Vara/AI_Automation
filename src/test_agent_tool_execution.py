from automation.ai.ai_brain import AIBrain
from automation.ai.llm.ollama_adapter import OllamaAdapter
from automation.ai.tools.shell_tool import ShellTool


def main():
    print("=== Agent Tool Execution E2E Test ===")

    llm = OllamaAdapter(model="qwen2.5:7b")
    brain = AIBrain(llm=llm)

    shell = ShellTool()
    brain.register_tool(shell)

    user_request = "Show me my current working directory"

    print(f"\nUser: {user_request}")
    print("\nSending request to Qwen...")

    response = brain.ask(user_request)

    print("\nLLM Response:")
    print(response.content)

    print("\nMetadata:")
    print(response.metadata)

    assert response.success

    assert response.metadata.get(
        "response_type"
    ) == "tool_call"

    tool_call = response.metadata.get(
        "tool_call"
    )

    assert tool_call is not None
    assert tool_call["tool"] == "Shell"

    tool_result = response.metadata.get(
        "tool_result"
    )

    assert tool_result is not None
    assert tool_result["success"] is True

    print("\n[PASS] LLM generated tool call")
    print("[PASS] Tool call executed")
    print("[PASS] Tool result returned to AIBrain")
    print("[PASS] Tool execution E2E flow works")

    print("\nAGENT TOOL EXECUTION E2E TEST PASSED")


if __name__ == "__main__":
    main()
