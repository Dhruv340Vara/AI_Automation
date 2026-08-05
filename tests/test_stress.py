from __future__ import annotations

import time

from automation.automation_runtime import (
    AutomationRuntime,
)

from automation.events.event import (
    Event,
)

from automation.events.event_types import (
    EventType,
)

print("=" * 60)
print("                STRESS TEST")
print("=" * 60)

runtime = AutomationRuntime()

received = []


def handler(event):

    received.append(event)


runtime.event_registry.register(
    EventType.MANUAL,
    handler,
)

runtime.start()

TOTAL_EVENTS = 1000

start = time.perf_counter()

for i in range(TOTAL_EVENTS):

    event = Event(

        event_type=EventType.MANUAL,

        source="stress",

        payload={

            "index": i,

        },

    )

    assert runtime.emit_event(
        event
    )

end = time.perf_counter()

runtime.stop()

duration = end - start

print()

print("Events Sent     :", TOTAL_EVENTS)
print("Events Received :", len(received))
print("Duration (sec)  :", round(duration, 3))
print(
    "Events / Second :",
    round(TOTAL_EVENTS / duration, 2),
)

assert len(received) == TOTAL_EVENTS

print()

print("=" * 60)
print("STRESS TEST PASSED")
print("=" * 60)
