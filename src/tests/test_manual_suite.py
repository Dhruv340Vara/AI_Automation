from __future__ import annotations

import time

from automation.automation_runtime import (
    AutomationRuntime,
)

from automation.events.event_types import (
    EventType,
)

from automation.triggers.manual_trigger import (
    ManualTrigger,
)

print("=" * 60)
print("          MANUAL TRIGGER TEST SUITE")
print("=" * 60)

runtime = AutomationRuntime()

handled_events = []


def handler(event):

    handled_events.append(event)

    print(
        "[Handler]",
        event.event_type.value,
    )

    print(
        event.payload,
    )


runtime.event_registry.register(
    EventType.MANUAL,
    handler,
)

trigger = ManualTrigger(

    name="Backup",

    description="Manual Backup",

)

runtime.register_manual_trigger(
    trigger
)

runtime.start()

print("\nRuntime Started")

runtime.trigger_manual(

    "Backup",

    user="Dhruv",

    metadata={

        "source": "test",

    },

)

timeout = time.time() + 5

while (
    len(handled_events) == 0
    and time.time() < timeout
):

    time.sleep(0.1)

runtime.stop()

assert len(
    handled_events
) == 1

event = handled_events[0]

assert (
    event.event_type
    == EventType.MANUAL
)

assert (
    event.payload["trigger"]
    == "Backup"
)

assert (
    event.payload["user"]
    == "Dhruv"
)

assert (
    event.payload["metadata"]["source"]
    == "test"
)

print()

print("All Assertions Passed")

print(
    "Handled Events:",
    len(handled_events),
)

print()

print("=" * 60)

print("MANUAL TRIGGER TEST SUITE PASSED")

print("=" * 60)
