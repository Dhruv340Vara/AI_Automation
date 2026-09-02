from automation.ai.memory_engine import MemoryEngine


engine = MemoryEngine()

print("\n=== Memory Access Tracking Test ===\n")


# Clean conversation memories
engine.clear_memory_type("conversation")


# --------------------------------------------------
# 1. Create memory
# --------------------------------------------------

print("1. Creating memory")

memory_id = engine.remember_conversation(
    role="user",
    content="My name is Dhruv.",
)

print("Memory ID:", memory_id)


# Check initial state
memories = engine.memories_by_type(
    "conversation"
)

memory = memories[0]

print(
    "Initial access_count:",
    memory.get("access_count"),
)


if memory.get("access_count") == 0:
    print("[PASS] Initial access_count is 0")
else:
    print("[FAIL] Initial access_count is not 0")


# --------------------------------------------------
# 2. Search memory first time
# --------------------------------------------------

print("\n2. First memory search")

results = engine.search_conversation(
    query="What is my name?",
    limit=5,
)

if results:
    print("[PASS] Memory retrieved")
else:
    print("[FAIL] Memory was not retrieved")


# Check access count
memories = engine.memories_by_type(
    "conversation"
)

memory = memories[0]

print(
    "access_count:",
    memory.get("access_count"),
)

print(
    "last_accessed_at:",
    memory.get("last_accessed_at"),
)


if memory.get("access_count") == 1:
    print("[PASS] access_count increased to 1")
else:
    print("[FAIL] access_count did not increase")


# --------------------------------------------------
# 3. Search again
# --------------------------------------------------

print("\n3. Second memory search")

results = engine.search_conversation(
    query="Tell me my name",
    limit=5,
)

if results:
    print("[PASS] Memory retrieved again")
else:
    print("[FAIL] Memory was not retrieved")


memories = engine.memories_by_type(
    "conversation"
)

memory = memories[0]

print(
    "access_count:",
    memory.get("access_count"),
)


if memory.get("access_count") == 2:
    print("[PASS] access_count increased to 2")
else:
    print("[FAIL] access_count is incorrect")


# --------------------------------------------------
# 4. Final state
# --------------------------------------------------

print("\n4. Final memory state")

memories = engine.memories_by_type(
    "conversation"
)

for memory in memories:
    print(
        f"- {memory.get('content')}"
    )
    print(
        f"  access_count = "
        f"{memory.get('access_count')}"
    )
    print(
        f"  last_accessed_at = "
        f"{memory.get('last_accessed_at')}"
    )


print("\n======================================")
print("MEMORY ACCESS TRACKING TEST COMPLETED")
print("======================================")
