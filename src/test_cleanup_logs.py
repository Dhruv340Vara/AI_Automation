from automation.ai.memory_engine import MemoryEngine


print("=== Cleanup Log Management Test ===")

engine = MemoryEngine()

# Backup existing memory data.
original_data = engine.store.load()

try:

    # Start isolated test storage.
    engine.store.save({})

    print("1. Creating cleanup logs")

    # Create 60 cleanup logs.
    for i in range(60):

        engine._log_cleanup(
            deleted_count=i % 3,
            scanned_count=10 + i,
            max_logs=50,
        )

    print("[PASS] Cleanup logs created")

    # -------------------------------------------------
    # Check retention
    # -------------------------------------------------

    logs = engine.cleanup_logs(
        limit=100
    )

    print(
        f"2. Logs remaining: {len(logs)}"
    )

    assert len(logs) == 50

    print(
        "[PASS] Only 50 logs retained"
    )

    # -------------------------------------------------
    # Check newest-first order
    # -------------------------------------------------

    timestamps = [
        log.get("created_at", "")
        for log in logs
    ]

    assert timestamps == sorted(
        timestamps,
        reverse=True,
    )

    print(
        "[PASS] Logs sorted newest-first"
    )

    # -------------------------------------------------
    # Check statistics
    # -------------------------------------------------

    stats = engine.cleanup_statistics()

    print("3. Cleanup statistics:")

    print(
        f"- total_runs: "
        f"{stats['total_runs']}"
    )

    print(
        f"- total_scanned: "
        f"{stats['total_scanned']}"
    )

    print(
        f"- total_deleted: "
        f"{stats['total_deleted']}"
    )

    assert stats["total_runs"] == 50

    print(
        "[PASS] Statistics calculated correctly"
    )

    # -------------------------------------------------
    # Check log structure
    # -------------------------------------------------

    first_log = logs[0]

    assert (
        first_log["type"]
        == "system_log"
    )

    assert (
        first_log["log_type"]
        == "memory_cleanup"
    )

    assert (
        "created_at"
        in first_log
    )

    assert (
        "deleted_count"
        in first_log
    )

    assert (
        "scanned_count"
        in first_log
    )

    print(
        "[PASS] Log structure is valid"
    )

    print()
    print(
        "CLEANUP LOG MANAGEMENT TEST PASSED"
    )

finally:

    # Restore user's real memory data.
    engine.store.save(
        original_data
    )
