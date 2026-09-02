from automation.ai.ai_brain import AIBrain
from automation.ai.llm.llm_adapter import LLMAdapter
from automation.ai.llm.llm_response import LLMResponse


class FakeLLM(LLMAdapter):

    def __init__(self, response_content):
        self.response_content = response_content

    def generate(self, message):
        return LLMResponse(
            success=True,
            content=self.response_content,
        )

    def available(self):
        return True


def main():
    print("=== AIBrain Tool Selection Integration Test ===")

    # Tool call response
    brain = AIBrain(
        llm=FakeLLM(
            '{"type":"tool_call","tool":"Shell","arguments":{"command":"pwd"}}'
        )
    )

    response = brain.ask("What is my current directory?")

    assert response.success
    assert response.get_metadata("response_type") == "tool_call"

    tool_call = response.get_metadata("tool_call")

    assert tool_call["tool"] == "Shell"
    assert tool_call["arguments"]["command"] == "pwd"

    print("[PASS] Tool call integrated into AIBrain")

    # Final answer response
    brain = AIBrain(
        llm=FakeLLM(
            '{"type":"final_answer","content":"Hello!"}'
        )
    )

    response = brain.ask("Hello")

    assert response.success
    assert response.get_metadata("response_type") == "final_answer"
    assert response.get_metadata("final_answer") == "Hello!"

    print("[PASS] Final answer integrated into AIBrain")

    print("AIBRAIN TOOL SELECTION INTEGRATION TEST PASSED")


if __name__ == "__main__":
    main()
