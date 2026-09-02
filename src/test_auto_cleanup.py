from automation.ai.memory_engine import MemoryEngine


print("=== Automatic Memory Cleanup Test ===")

engine = MemoryEngine()

# Start automatic cleanup with a very short interval
# for testing purposes.
engine.start_auto_cleanup(
    interval_hours=0.0003,
    min_importance=0.30,
    max_age_days=30,
)

print("1. Automatic cleanup started")

thread = getattr(
    engine,
    "_cleanup_thread",
    None,
)

assert thread is not None
assert thread.is_alive()

print("[PASS] Cleanup thread is running")


# Wait until at least one cleanup cycle runs.
import time

time.sleep(2)

logs = engine.cleanup_logs(limit=10)

print(
    f"2. Cleanup logs found: {len(logs)}"
)

assert len(logs) >= 1

print("[PASS] Automatic cleanup executed")


for log in logs:

    print(
        f"- {log.get('created_at')} "
        f"| scanned={log.get('scanned_count')} "
        f"| deleted={log.get('deleted_count')}"
    )


# Stop cleanup.
engine.stop_auto_cleanup()

print("3. Automatic cleanup stopped")

thread = getattr(
    engine,
    "_cleanup_thread",
    None,
)

assert thread is None

print("[PASS] Cleanup thread stopped")

print()
print("AUTOMATIC CLEANUP TEST PASSED")
