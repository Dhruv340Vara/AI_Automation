from automation.ai.llm.ollama_adapter import OllamaAdapter
from automation.ai.llm.llm_message import LLMMessage


def main():
    print("=== Tool Schema Context Test ===")

    adapter = OllamaAdapter(model="qwen2.5:7b")

    message = LLMMessage(
        system="You are an AI assistant with access to external tools.",
        user="test",
        context={
            "conversation": [],
            "memories": [],
            "tools": [
                {
                    "name": "Shell",
                    "description": "Execute an approved shell command.",
                },
                {
                    "name": "Memory",
                    "description": "Store and retrieve user memories.",
                },
            ],
        },
    )

    print("Context:")
    print(message.context)

    prompt = adapter._build_prompt(message)

    print("\nGenerated Prompt:\n")
    print(prompt)

    assert "Available Tools:" in prompt
    assert "Shell: Execute an approved shell command." in prompt
    assert "Memory: Store and retrieve user memories." in prompt

    print("\n[PASS] Tool schemas injected into prompt")
    print("TOOL SCHEMA INJECTION TEST PASSED")


if __name__ == "__main__":
    main()