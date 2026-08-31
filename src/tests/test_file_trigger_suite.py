from __future__ import annotations

import shutil
import time
from pathlib import Path

from automation.automation_runtime import (
    AutomationRuntime,
)
from automation.events import (
    EventType,
)
from automation.triggers import (
    FileTrigger,
)

print("=" * 60)
print("        FILE TRIGGER TEST SUITE")
print("=" * 60)

TEST_DIR = Path("test_file_trigger_suite")

if TEST_DIR.exists():
    shutil.rmtree(TEST_DIR)

TEST_DIR.mkdir()

runtime = AutomationRuntime()

handled = []


def file_handler(event):

    handled.append(event)

    print(
        "[Handler]",
        event.event_type.value,
        event.payload,
    )


runtime.event_registry.register(
    EventType.FILE_CREATED,
    file_handler,
)

trigger = FileTrigger(
    name="Suite Test",
    path=str(TEST_DIR),
    events=["created"],
    recursive=False,
)

runtime.register_file_trigger(
    trigger
)

runtime.start()

print("\nRuntime Started")

time.sleep(1)

test_file = TEST_DIR / "demo.txt"

print(
    "\nCreating:",
    test_file.name,
)

test_file.write_text(
    "Hello AI Assistant"
)

timeout = time.time() + 5

while (
    len(handled) == 0
    and time.time() < timeout
):
    time.sleep(0.1)

runtime.stop()

assert len(handled) == 1

assert (
    handled[0].event_type
    == EventType.FILE_CREATED
)

assert (
    handled[0].payload["path"]
    == str(test_file)
)

print("\nAssertions Passed")

print(
    "Detected Events:",
    len(handled),
)

print(
    "\nFILE TRIGGER TEST SUITE PASSED"
)

shutil.rmtree(TEST_DIR)
