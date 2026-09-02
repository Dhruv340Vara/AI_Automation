from automation.ai.ai_brain import AIBrain
from automation.ai.llm.ollama_adapter import OllamaAdapter
from automation.ai.tools.shell_tool import ShellTool


def main():
    print("=== Ollama Actual Tool Selection Test ===")

    llm = OllamaAdapter(model="qwen2.5:7b")
    brain = AIBrain(llm=llm)

    # Register an actual available tool
    shell_tool = ShellTool()
    brain.register_tool(shell_tool)

    print("\nAvailable tools:")
    print(brain.available_tools())

    user_request = "Show me my current working directory"

    print(f"\nUser: {user_request}")
    print("\nSending request to Qwen...")

    response = brain.ask(user_request)

    print("\nLLM Response:")
    print(response.content)

    print("\nMetadata:")
    print(response.metadata)

    assert response.success, "LLM request failed"

    response_type = response.metadata.get("response_type")

    assert response_type == "tool_call", (
        f"Expected tool_call, got {response_type}"
    )

    tool_call = response.metadata.get("tool_call")

    assert tool_call is not None, "Tool call metadata missing"

    selected_tool = tool_call.get("tool")

    print(f"\nSelected tool: {selected_tool}")

    assert selected_tool == shell_tool.name, (
        f"Unexpected tool selected: {selected_tool}"
    )

    print("[PASS] Qwen selected an available tool")
    print(f"[PASS] Selected tool: {selected_tool}")
    print("[PASS] No invented tool selected")

    print("\nOLLAMA ACTUAL TOOL SELECTION TEST PASSED")


if __name__ == "__main__":
    main()