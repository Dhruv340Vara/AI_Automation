from automation.ai.memory_engine import MemoryEngine


print("=== Memory Retrieval Filter Test ===")

engine = MemoryEngine()

original_data = engine.store.load()

try:

    # Isolated test environment.
    engine.store.save({})

    # -------------------------------------------------
    # 1. Create old memory
    # -------------------------------------------------

    old_id = engine.remember_conversation(
        role="user",
        content="I prefer Python.",
    )

    print("1. Old memory created")
    print(f"Old ID: {old_id}")

    # -------------------------------------------------
    # 2. Create new conflicting memory
    # -------------------------------------------------

    new_id = engine.remember_conversation(
        role="user",
        content="I prefer PHP.",
    )

    print("2. New memory created")
    print(f"New ID: {new_id}")

    # -------------------------------------------------
    # 3. Verify old memory is superseded
    # -------------------------------------------------

    data = engine.store.load()

    assert (
        data[old_id].get("status")
        == "superseded"
    )

    assert (
        data[new_id].get(
            "status",
            "active",
        )
        == "active"
    )

    print(
        "[PASS] Memory statuses are correct"
    )

    # -------------------------------------------------
    # 4. Search
    # -------------------------------------------------

    results = engine.search_conversation(
        query="I prefer Python or PHP",
        limit=10,
    )

    print(
        f"3. Search results: {len(results)}"
    )

    # -------------------------------------------------
    # 5. Superseded memory must not appear
    # -------------------------------------------------

    result_ids = {
        memory.get("id")
        for memory in results
    }

    assert old_id not in result_ids

    print(
        "[PASS] Superseded memory filtered"
    )

    # -------------------------------------------------
    # 6. New memory must appear
    # -------------------------------------------------

    assert new_id in result_ids

    print(
        "[PASS] Active memory retrieved"
    )

    # -------------------------------------------------
    # 7. Verify every result is active
    # -------------------------------------------------

    for memory in results:

        assert memory.get(
            "status",
            "active",
        ) == "active"

    print(
        "[PASS] All retrieved memories are active"
    )

    # -------------------------------------------------
    # 8. Verify old memory still exists
    # -------------------------------------------------

    data = engine.store.load()

    assert old_id in data

    print(
        "[PASS] Superseded memory preserved in storage"
    )

    print()
    print(
        "MEMORY RETRIEVAL FILTER TEST PASSED"
    )

finally:

    # Restore real memories.
    engine.store.save(original_data)
