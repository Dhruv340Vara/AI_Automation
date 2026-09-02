from automation.ai.ai_brain import AIBrain


def main():
    brain = AIBrain()

    prompt = brain._tool_selection_system_prompt()

    print("=== Tool Selection Prompt Test ===")
    print(prompt)

    assert "tool_call" in prompt
    assert "final_answer" in prompt
    assert "available tools" in prompt.lower()
    assert "JSON" in prompt

    print("[PASS] Tool selection prompt created")
    print("TOOL SELECTION PROMPT TEST PASSED")


if __name__ == "__main__":
    main()
