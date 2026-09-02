from automation.ai.memory_engine import MemoryEngine


engine = MemoryEngine()

print("\n=== Smart Memory Test ===\n")


# Clean conversation memories
engine.clear_memory_type("conversation")


# --------------------------------------------------
# 1. First memory
# --------------------------------------------------

print("1. Saving first memory")

first_id = engine.remember_conversation(
    role="user",
    content="My name is Dhruv.",
)

print("First ID:", first_id)


# --------------------------------------------------
# 2. Same memory again
# --------------------------------------------------

print("\n2. Saving duplicate memory")

second_id = engine.remember_conversation(
    role="user",
    content="My name is Dhruv.",
)

print("Second ID:", second_id)


if first_id == second_id:
    print("[PASS] Duplicate updated existing memory")
else:
    print("[FAIL] Duplicate created a new memory")


# --------------------------------------------------
# 3. Check memory count
# --------------------------------------------------

print("\n3. Checking memory count")

memories = engine.memories_by_type(
    "conversation"
)

print("Memory count:", len(memories))

if len(memories) == 1:
    print("[PASS] Only one memory exists")
else:
    print("[FAIL] Duplicate memory exists")


# --------------------------------------------------
# 4. Different memory
# --------------------------------------------------

print("\n4. Saving different memory")

third_id = engine.remember_conversation(
    role="user",
    content="I like Python.",
)

if third_id != first_id:
    print("[PASS] Different memory created")
else:
    print("[FAIL] Different memory incorrectly matched")


# --------------------------------------------------
# 5. Final memories
# --------------------------------------------------

print("\n5. Final memories")

memories = engine.memories_by_type(
    "conversation"
)

for memory in memories:
    print(
        f"- [{memory.get('memory_type')}] "
        f"{memory.get('content')}"
    )


print("\n======================================")
print("SMART MEMORY TEST COMPLETED")
print("======================================")

