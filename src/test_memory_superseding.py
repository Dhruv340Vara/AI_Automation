from automation.ai.memory_engine import MemoryEngine


print("=== Memory Superseding Test ===")

engine = MemoryEngine()

original_data = engine.store.load()

try:

    # Isolated test environment.
    engine.store.save({})

    # -------------------------------------------------
    # 1. Create original memory
    # -------------------------------------------------

    old_id = engine.remember_conversation(
        role="user",
        content="I prefer Python.",
    )

    print("1. Original memory created")
    print(f"Old ID: {old_id}")

    data = engine.store.load()

    assert old_id in data
    assert data[old_id].get(
        "status",
        "active"
    ) == "active"

    print(
        "[PASS] Original memory is active"
    )

    # -------------------------------------------------
    # 2. Create conflicting memory
    # -------------------------------------------------

    new_id = engine.remember_conversation(
        role="user",
        content="I prefer PHP.",
    )

    print("2. New conflicting memory created")
    print(f"New ID: {new_id}")

    assert new_id != old_id

    print(
        "[PASS] New memory has different ID"
    )

    # -------------------------------------------------
    # 3. Check old memory
    # -------------------------------------------------

    data = engine.store.load()

    old_memory = data[old_id]

    print("3. Checking old memory")

    assert (
        old_memory.get("status")
        == "superseded"
    )

    print(
        "[PASS] Old memory marked superseded"
    )

    assert (
        old_memory.get("superseded_by")
        == new_id
    )

    print(
        "[PASS] superseded_by points to new memory"
    )

    assert (
        "superseded_at"
        in old_memory
    )

    print(
        "[PASS] superseded_at recorded"
    )

    # -------------------------------------------------
    # 4. Check new memory
    # -------------------------------------------------

    new_memory = data[new_id]

    print("4. Checking new memory")

    assert (
        new_memory.get("status", "active")
        == "active"
    )

    print(
        "[PASS] New memory remains active"
    )

    assert (
        new_memory.get("content")
        == "I prefer PHP."
    )

    print(
        "[PASS] New memory content is correct"
    )

    # -------------------------------------------------
    # 5. Old memory must still exist
    # -------------------------------------------------

    assert old_id in data

    print(
        "[PASS] Old memory preserved for history"
    )

    print()
    print(
        "MEMORY SUPERSEDING TEST PASSED"
    )

finally:

    # Restore user's real memories.
    engine.store.save(original_data)
