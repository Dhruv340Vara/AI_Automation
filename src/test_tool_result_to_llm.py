from automation.ai.ai_brain import AIBrain
from automation.ai.llm.ollama_adapter import OllamaAdapter
from automation.ai.tools.shell_tool import ShellTool


print("=== Tool Result → LLM Test ===")

llm = OllamaAdapter(
    model="qwen2.5:7b"
)

brain = AIBrain(
    llm=llm
)

brain.register_tool(
    ShellTool()
)

user_query = "Show me my current working directory"

print(f"User: {user_query}")

response = brain.ask(user_query)

print("\nFirst LLM Response:")
print(response.content)

print("\nMetadata:")
print(response.metadata)

if not response.success:
    print("[FAIL] Initial LLM request failed")
    raise SystemExit(1)

tool_call = response.get_metadata(
    "tool_call"
)

tool_result = response.get_metadata(
    "tool_result"
)

if not tool_call:
    print("[FAIL] No tool call generated")
    raise SystemExit(1)

print("\n[PASS] Tool call generated")

if not tool_result:
    print("[FAIL] No tool result returned")
    raise SystemExit(1)

print("[PASS] Tool result returned")

print("\nTool Result:")
print(tool_result)

print("\n=== TEST COMPLETE ===")
