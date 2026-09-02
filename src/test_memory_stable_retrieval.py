from automation.ai.memory_engine import MemoryEngine


engine = MemoryEngine()

print("\n=== Stable Retrieval Test ===\n")


# --------------------------------------------------
# Clean test data
# --------------------------------------------------

engine.clear_memory_type(
    "conversation"
)


# --------------------------------------------------
# Create two similar memories
# --------------------------------------------------

first_id = engine.remember_conversation(
    role="user",
    content="I like Python programming.",
    importance=0.85,
)

second_id = engine.remember_conversation(
    role="user",
    content="I like Python development.",
    importance=0.85,
)


print("1. Created memories")

print("First ID:", first_id)
print("Second ID:", second_id)


# --------------------------------------------------
# Check initial access counts
# --------------------------------------------------

memories = engine.memories_by_type(
    "conversation"
)

print("\n2. Initial access counts")

for memory in memories:
    print(
        f"- {memory['content']}"
    )
    print(
        f"  access_count = "
        f"{memory.get('access_count', 0)}"
    )


# --------------------------------------------------
# First search
# --------------------------------------------------

print("\n3. First search")

results = engine.search_conversation(
    query="Python",
    limit=1,
)

if not results:
    print(
        "[FAIL] No memory returned"
    )
    raise SystemExit(1)


first_result = results[0]

print(
    "Returned:",
    first_result["content"],
)

print(
    "Returned access_count:",
    first_result.get(
        "access_count",
        0,
    ),
)


# --------------------------------------------------
# Check stored access count
# --------------------------------------------------

memories = engine.memories_by_type(
    "conversation"
)

access_counts = {
    memory["id"]: memory.get(
        "access_count",
        0,
    )
    for memory in memories
}


print("\n4. Access counts after first search")

for memory in memories:
    print(
        f"- {memory['content']}"
    )
    print(
        f"  access_count = "
        f"{memory.get('access_count', 0)}"
    )


total_accesses = sum(
    access_counts.values()
)


if total_accesses == 1:
    print(
        "[PASS] Exactly one memory was accessed"
    )
else:
    print(
        "[FAIL] Unexpected access count"
    )


# --------------------------------------------------
# Second search
# --------------------------------------------------

print("\n5. Second search")

results = engine.search_conversation(
    query="Python",
    limit=1,
)

if not results:
    print(
        "[FAIL] No memory returned"
    )
    raise SystemExit(1)


second_result = results[0]

print(
    "Returned:",
    second_result["content"],
)


# --------------------------------------------------
# Final access counts
# --------------------------------------------------

memories = engine.memories_by_type(
    "conversation"
)

print("\n6. Final access counts")

for memory in memories:
    print(
        f"- {memory['content']}"
    )
    print(
        f"  access_count = "
        f"{memory.get('access_count', 0)}"
    )


final_total = sum(
    memory.get(
        "access_count",
        0,
    )
    for memory in memories
)


if final_total == 2:
    print(
        "[PASS] Access tracking is stable"
    )
else:
    print(
        "[FAIL] Access tracking is incorrect"
    )


print("\n======================================")
print("STABLE RETRIEVAL TEST COMPLETED")
print("======================================")
