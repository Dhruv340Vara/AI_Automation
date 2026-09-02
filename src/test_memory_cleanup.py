from datetime import datetime, timedelta

from automation.ai.memory_engine import MemoryEngine


print("=== Memory Cleanup Test ===")

engine = MemoryEngine()

# Backup existing memories so the test is safe.
original_data = engine.store.load()

try:
    # Start with clean test data.
    engine.store.save({})

    now = datetime.now()

    # -------------------------------------------------
    # 1. Old low-importance conversation
    # -------------------------------------------------

    old_conversation_id = "test-old-conversation"

    engine.store.save({
        old_conversation_id: {
            "id": old_conversation_id,
            "type": "conversation",
            "memory_type": "conversation",
            "role": "user",
            "content": "Old useless conversation",
            "importance": 0.10,
            "created_at": (
                now - timedelta(days=60)
            ).isoformat(timespec="seconds"),
            "updated_at": (
                now - timedelta(days=60)
            ).isoformat(timespec="seconds"),
            "last_accessed_at": (
                now - timedelta(days=60)
            ).isoformat(timespec="seconds"),
            "access_count": 0,
            "metadata": {},
        }
    })

    # -------------------------------------------------
    # 2. Important fact
    # -------------------------------------------------

    important_id = "test-important-fact"

    data = engine.store.load()

    data[important_id] = {
        "id": important_id,
        "type": "conversation",
        "memory_type": "fact",
        "role": "user",
        "content": "My name is Dhruv.",
        "importance": 0.95,
        "created_at": (
            now - timedelta(days=60)
        ).isoformat(timespec="seconds"),
        "updated_at": (
            now - timedelta(days=60)
        ).isoformat(timespec="seconds"),
        "last_accessed_at": (
            now - timedelta(days=60)
        ).isoformat(timespec="seconds"),
        "access_count": 0,
        "metadata": {},
    }

    # -------------------------------------------------
    # 3. Old but already accessed memory
    # -------------------------------------------------

    accessed_id = "test-accessed-memory"

    data[accessed_id] = {
        "id": accessed_id,
        "type": "conversation",
        "memory_type": "conversation",
        "role": "user",
        "content": "Old Python discussion",
        "importance": 0.10,
        "created_at": (
            now - timedelta(days=60)
        ).isoformat(timespec="seconds"),
        "updated_at": (
            now - timedelta(days=60)
        ).isoformat(timespec="seconds"),
        "last_accessed_at": (
            now - timedelta(days=10)
        ).isoformat(timespec="seconds"),
        "access_count": 2,
        "metadata": {},
    }

    engine.store.save(data)

    print("1. Test memories created")
    print("PASS")

    # -------------------------------------------------
    # 4. Run cleanup
    # -------------------------------------------------

    deleted = engine.cleanup_memories(
        min_importance=0.30,
        max_age_days=30,
    )

    print(f"2. Deleted memories: {deleted}")

    assert deleted == 1

    print("[PASS] Exactly one memory deleted")

    # -------------------------------------------------
    # 5. Verify deleted memory
    # -------------------------------------------------

    data = engine.store.load()

    assert old_conversation_id not in data

    print(
        "[PASS] Old low-importance memory deleted"
    )

    # -------------------------------------------------
    # 6. Verify important memory
    # -------------------------------------------------

    assert important_id in data

    print(
        "[PASS] Important fact protected"
    )

    # -------------------------------------------------
    # 7. Verify accessed memory
    # -------------------------------------------------

    assert accessed_id in data

    print(
        "[PASS] Accessed memory protected"
    )

    print()
    print("MEMORY CLEANUP TEST PASSED")

finally:
    # Restore user's original memories.
    engine.store.save(original_data)
