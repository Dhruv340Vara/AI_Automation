from automation.ai.memory_engine import MemoryEngine


print("=== Memory Conflict Resolution E2E Test ===")

engine = MemoryEngine()

# Backup real memory data.
original_data = engine.store.load()

try:

    # Isolated test environment.
    engine.store.save({})

    # =================================================
    # 1. Preference conflict
    # =================================================

    print("\n1. Testing preference conflict")

    python_id = engine.remember_conversation(
        role="user",
        content="I prefer Python.",
    )

    php_id = engine.remember_conversation(
        role="user",
        content="I prefer PHP.",
    )

    data = engine.store.load()

    assert data[python_id]["status"] == "superseded"
    assert data[python_id]["superseded_by"] == php_id

    assert data[php_id].get(
        "status",
        "active",
    ) == "active"

    print(
        "[PASS] Preference conflict resolved"
    )

    # Retrieval must return PHP, not Python.
    results = engine.search_conversation(
        query="I prefer Python or PHP",
        limit=10,
    )

    result_ids = {
        memory["id"]
        for memory in results
    }

    assert python_id not in result_ids
    assert php_id in result_ids

    print(
        "[PASS] Retrieval returns only active preference"
    )

    # =================================================
    # 2. Fact conflict
    # =================================================

    print("\n2. Testing fact conflict")

    old_location_id = engine.remember_conversation(
        role="user",
        content="I live in Ahmedabad.",
    )

    new_location_id = engine.remember_conversation(
        role="user",
        content="I live in Surat now.",
    )

    data = engine.store.load()

    assert (
        data[old_location_id]["status"]
        == "superseded"
    )

    assert (
        data[old_location_id]["superseded_by"]
        == new_location_id
    )

    assert (
        data[new_location_id].get(
            "status",
            "active",
        )
        == "active"
    )

    print(
        "[PASS] Fact conflict resolved"
    )

    # =================================================
    # 3. Goal conflict
    # =================================================

    print("\n3. Testing goal conflict")

    old_goal_id = engine.remember_conversation(
        role="user",
        content="I am building an automation system.",
    )

    new_goal_id = engine.remember_conversation(
        role="user",
        content="I am building a cybersecurity system.",
    )

    data = engine.store.load()

    assert (
        data[old_goal_id]["status"]
        == "superseded"
    )

    assert (
        data[old_goal_id]["superseded_by"]
        == new_goal_id
    )

    assert (
        data[new_goal_id].get(
            "status",
            "active",
        )
        == "active"
    )

    print(
        "[PASS] Goal conflict resolved"
    )

    # =================================================
    # 4. Instruction conflict
    # =================================================

    print("\n4. Testing instruction conflict")

    old_instruction_id = (
        engine.remember_conversation(
            role="user",
            content="From now on use Python.",
        )
    )

    new_instruction_id = (
        engine.remember_conversation(
            role="user",
            content="From now on use PHP.",
        )
    )

    data = engine.store.load()

    assert (
        data[old_instruction_id]["status"]
        == "superseded"
    )

    assert (
        data[old_instruction_id]["superseded_by"]
        == new_instruction_id
    )

    assert (
        data[new_instruction_id].get(
            "status",
            "active",
        )
        == "active"
    )

    print(
        "[PASS] Instruction conflict resolved"
    )

    # =================================================
    # 5. Duplicate must NOT create conflict
    # =================================================

    print("\n5. Testing duplicate memory")

    duplicate_id = engine.remember_conversation(
        role="user",
        content="I prefer PHP.",
    )

    assert duplicate_id == php_id

    data = engine.store.load()

    assert len(data) == 8

    print(
        "[PASS] Duplicate memory reused existing ID"
    )

    # =================================================
    # 6. Unrelated memory
    # =================================================

    print("\n6. Testing unrelated memory")

    discussion_id = engine.remember_conversation(
        role="user",
        content="Let's discuss artificial intelligence.",
    )

    data = engine.store.load()

    assert (
        data[discussion_id].get(
            "status",
            "active",
        )
        == "active"
    )

    print(
        "[PASS] Unrelated memory remains active"
    )

    # =================================================
    # 7. Verify superseded memories remain stored
    # =================================================

    print(
        "\n7. Checking historical memory preservation"
    )

    data = engine.store.load()

    superseded_count = sum(
        1
        for memory in data.values()
        if isinstance(memory, dict)
        and memory.get("status")
        == "superseded"
    )

    active_count = sum(
        1
        for memory in data.values()
        if isinstance(memory, dict)
        and memory.get(
            "status",
            "active",
        )
        == "active"
    )

    print(
        f"Superseded memories: {superseded_count}"
    )

    print(
        f"Active memories: {active_count}"
    )

    assert superseded_count == 4

    print(
        "[PASS] Superseded history preserved"
    )

    # =================================================
    # Final
    # =================================================

    print()
    print(
        "MEMORY CONFLICT RESOLUTION E2E TEST PASSED"
    )

finally:

    # Restore user's real memory data.
    engine.store.save(original_data)
