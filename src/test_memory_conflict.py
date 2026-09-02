from automation.ai.memory_engine import MemoryEngine


print("=== Memory Conflict Detection Test ===")

engine = MemoryEngine()

original_data = engine.store.load()

try:

    # Isolated test environment.
    engine.store.save({})

    # -------------------------------------------------
    # Create first preference
    # -------------------------------------------------

    first_id = engine.remember_conversation(
        role="user",
        content="I prefer Python.",
    )

    print("1. First preference created")
    print(f"ID: {first_id}")

    # -------------------------------------------------
    # Search for possible conflict
    # -------------------------------------------------

    conflicts = engine.find_conflicting_memories(
        content="I prefer PHP.",
        memory_type="preference",
    )

    print(
        f"2. Conflicts found: {len(conflicts)}"
    )

    assert len(conflicts) == 1

    print(
        "[PASS] Potential conflict detected"
    )

    assert (
        conflicts[0]["content"]
        == "I prefer Python."
    )

    print(
        "[PASS] Correct memory identified"
    )

    # -------------------------------------------------
    # Different category
    # -------------------------------------------------

    engine.remember_conversation(
        role="user",
        content="I am building an AI assistant.",
    )

    conflicts = engine.find_conflicting_memories(
        content="I prefer PHP.",
        memory_type="preference",
    )

    # Only preference should be considered.
    assert len(conflicts) == 1

    print(
        "[PASS] Different memory category ignored"
    )

    print()
    print(
        "MEMORY CONFLICT DETECTION TEST PASSED"
    )

finally:

    # Restore real memories.
    engine.store.save(original_data)
