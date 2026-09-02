from automation.ai.ai_brain import AIBrain
from automation.ai.llm.ollama_adapter import OllamaAdapter


brain = AIBrain(
    llm=OllamaAdapter(model="qwen2.5:7b"),
    max_history=10,
)

print("\n=== Dynamic Memory Test ===")

print("\n1. First conversation")

response = brain.ask("My name is Dhruv.")

print("User: My name is Dhruv.")
print("Assistant:", response.content)

assert response.success

print("\n2. Checking automatic memory saving")

memories = brain.memory.recent_memories(limit=10)

for memory in memories:
    print(
        f"- [{memory.get('role')}] "
        f"{memory.get('content')}"
    )

assert any(
    memory.get("content") == "My name is Dhruv."
    for memory in memories
)

print("PASS")


print("\n3. Testing memory retrieval")

response = brain.ask("What is my name?")

print("User: What is my name?")
print("Assistant:", response.content)

assert response.success
assert "Dhruv" in response.content

print("PASS")


print("\n4. Final memories")

memories = brain.memory.recent_memories(limit=10)

for memory in memories:
    print(
        f"- [{memory.get('role')}] "
        f"{memory.get('content')}"
    )

print("\n======================================")
print("DYNAMIC MEMORY TEST PASSED")
print("======================================")
