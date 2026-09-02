from automation.ai.memory_engine import MemoryEngine
from automation.ai.memory_store import MemoryStore


def main():
    print("\n=== MemoryEngine Test ===\n")

    # Temporary test memory file
    store = MemoryStore("memory/test_memory.json")
    engine = MemoryEngine(store)

    # Clean previous test data
    engine.clear()

    # --------------------------------------------------
    # 1. Basic key/value memory
    # --------------------------------------------------
    print("1. Basic Memory")

    engine.set("name", "Dhruv")

    print("Stored name:", engine.get("name"))
    print("Exists:", engine.exists("name"))

    assert engine.get("name") == "Dhruv"
    assert engine.exists("name")

    print("PASS\n")

    # --------------------------------------------------
    # 2. Conversation memories
    # --------------------------------------------------
    print("2. Conversation Memory")

    id1 = engine.remember_conversation(
        role="user",
        content="My name is Dhruv.",
        importance=0.8,
    )

    id2 = engine.remember_conversation(
        role="assistant",
        content="Nice to meet you Dhruv.",
        importance=0.5,
    )

    id3 = engine.remember_conversation(
        role="user",
        content="I am working on an AI automation project.",
        importance=0.9,
    )

    print("Memory IDs:")
    print(id1)
    print(id2)
    print(id3)

    assert id1
    assert id2
    assert id3

    print("PASS\n")

    # --------------------------------------------------
    # 3. Search conversation
    # --------------------------------------------------
    print("3. Search Conversation")

    results = engine.search_conversation("Dhruv")

    print("Search results:")
    for memory in results:
        print(memory)

    assert len(results) >= 1
    assert any("Dhruv" in memory["content"] for memory in results)

    print("PASS\n")

    # --------------------------------------------------
    # 4. Recent memories
    # --------------------------------------------------
    print("4. Recent Memories")

    recent = engine.recent_memories(limit=2)

    print("Recent memories:")
    for memory in recent:
        print(memory)

    assert len(recent) <= 2

    print("PASS\n")

    # --------------------------------------------------
    # 5. Memories by type
    # --------------------------------------------------
    print("5. Memories By Type")

    conversation_memories = engine.memories_by_type("conversation")

    print("Conversation memories:")
    for memory in conversation_memories:
        print(memory)

    assert len(conversation_memories) == 3

    print("PASS\n")

    # --------------------------------------------------
    # 6. Forget one memory
    # --------------------------------------------------
    print("6. Forget Memory")

    removed = engine.forget_memory(id2)

    print("Removed:", removed)

    assert removed is True
    assert len(engine.memories_by_type("conversation")) == 2

    print("PASS\n")

    # --------------------------------------------------
    # 7. Clear memory type
    # --------------------------------------------------
    print("7. Clear Conversation Memories")

    removed_count = engine.clear_memory_type("conversation")

    print("Removed count:", removed_count)

    assert removed_count == 2
    assert len(engine.memories_by_type("conversation")) == 0

    print("PASS\n")

    # --------------------------------------------------
    # 8. Basic memory should still exist
    # --------------------------------------------------
    print("8. Verify Basic Memory")

    assert engine.get("name") == "Dhruv"

    print("Name:", engine.get("name"))
    print("PASS\n")

    # --------------------------------------------------
    # Final cleanup
    # --------------------------------------------------
    engine.clear()

    print("================================")
    print("ALL MEMORY ENGINE TESTS PASSED")
    print("================================")


if __name__ == "__main__":
    main()
