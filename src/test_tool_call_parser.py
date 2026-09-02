from automation.ai.tool_call_parser import ToolCallParser


def main():
    print("=== LLM Structured Response Parser Test ===")

    # 1. Tool call
    tool_response = """
    {
        "type": "tool_call",
        "tool": "Shell",
        "arguments": {
            "command": "pwd"
        }
    }
    """

    result = ToolCallParser.parse(tool_response)

    assert result["type"] == "tool_call"
    assert result["tool_call"].tool == "Shell"
    assert result["tool_call"].arguments["command"] == "pwd"

    print("[PASS] Tool call parsed")

    # 2. Final answer
    final_response = """
    {
        "type": "final_answer",
        "content": "Hello! How can I help you?"
    }
    """

    result = ToolCallParser.parse(final_response)

    assert result["type"] == "final_answer"
    assert result["content"] == "Hello! How can I help you?"

    print("[PASS] Final answer parsed")

    # 3. Invalid JSON
    try:
        ToolCallParser.parse("not valid json")
        raise AssertionError("Invalid JSON was accepted")
    except ValueError:
        print("[PASS] Invalid JSON rejected")

    # 4. Unsupported type
    try:
        ToolCallParser.parse(
            '{"type": "unknown"}'
        )
        raise AssertionError("Unsupported type was accepted")
    except ValueError:
        print("[PASS] Unsupported response type rejected")

    print("LLM STRUCTURED RESPONSE PARSER TEST PASSED")


if __name__ == "__main__":
    main()
