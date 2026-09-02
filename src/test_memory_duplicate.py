from automation.ai.memory_engine import MemoryEngine


engine = MemoryEngine()

print("\n=== Duplicate Memory Test ===\n")

# Clean test memories
engine.clear_memory_type("conversation")


print("1. Saving first memory")

first_id = engine.remember_conversation(
    role="user",
    content="My name is Dhruv.",
)

print("First ID:", first_id)


print("\n2. Searching for duplicate")

duplicate = engine.find_similar_memory(
    content="My name is Dhruv.",
    memory_type="fact",
)

if duplicate:
    print("[PASS] Duplicate memory detected")
    print("Existing memory:", duplicate["content"])
else:
    print("[FAIL] Duplicate memory not detected")


print("\n3. Testing different memory")

different = engine.find_similar_memory(
    content="I like Python.",
    memory_type="preference",
)

if different is None:
    print("[PASS] Different memory correctly rejected")
else:
    print("[FAIL] Different memory incorrectly matched")


print("\n======================================")
print("DUPLICATE MEMORY TEST COMPLETED")
print("======================================")

