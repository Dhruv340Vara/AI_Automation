from automation.ai.memory_engine import MemoryEngine


engine = MemoryEngine()

print("\n=== Memory Ranking V2 Test ===\n")

engine.clear_memory_type("conversation")


# --------------------------------------------------
# Create memories
# --------------------------------------------------

memory_a = engine.remember_conversation(
    role="user",
    content="I like Python programming.",
    importance=0.85,
)

memory_b = engine.remember_conversation(
    role="user",
    content="I like PHP programming.",
    importance=0.85,
)


# --------------------------------------------------
# Access Python memory multiple times
# --------------------------------------------------

print("1. Accessing Python memory")

for _ in range(5):
    engine.search_conversation(
        query="Python",
        limit=5,
    )


# --------------------------------------------------
# Check access counts
# --------------------------------------------------

print("\n2. Checking access counts")

memories = engine.memories_by_type(
    "conversation"
)

for memory in memories:
    print(
        f"- {memory['content']}"
    )
    print(
        f"  access_count = "
        f"{memory.get('access_count', 0)}"
    )


# --------------------------------------------------
# Search Python
# --------------------------------------------------

print("\n3. Ranking Python memories")

results = engine.search_conversation(
    query="Python",
    limit=5,
)

for index, memory in enumerate(
    results,
    start=1,
):
    print(
        f"{index}. {memory['content']}"
    )
    print(
        f"   access_count = "
        f"{memory.get('access_count', 0)}"
    )


# --------------------------------------------------
# Validate
# --------------------------------------------------

if results:

    top_memory = results[0]

    if "Python" in top_memory["content"]:
        print(
            "\n[PASS] Python memory ranked first"
        )
    else:
        print(
            "\n[FAIL] Python memory not ranked first"
        )

else:
    print(
        "\n[FAIL] No memories returned"
    )


print("\n======================================")
print("MEMORY RANKING V2 TEST COMPLETED")
print("======================================")
