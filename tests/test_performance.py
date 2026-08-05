from __future__ import annotations

import statistics
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
print("             PERFORMANCE TEST")
print("=" * 60)

runtime = AutomationRuntime()

handled = []


def handler(event):

    handled.append(event)


runtime.event_registry.register(
    EventType.MANUAL,
    handler,
)

runtime.start()

TOTAL_EVENTS = 1000

times = []

overall_start = time.perf_counter()

for i in range(TOTAL_EVENTS):

    event = Event(

        event_type=EventType.MANUAL,

        source="performance",

        payload={

            "index": i,

        },

    )

    start = time.perf_counter()

    assert runtime.emit_event(event)

    end = time.perf_counter()

    times.append(
        end - start
    )

overall_end = time.perf_counter()

runtime.stop()

# ------------------------------------------------

total_time = overall_end - overall_start

average = statistics.mean(times)

minimum = min(times)

maximum = max(times)

throughput = TOTAL_EVENTS / total_time

# ------------------------------------------------

print()

print("Events           :", TOTAL_EVENTS)

print(
    "Handled          :",
    len(handled),
)

print()

print(
    "Total Time (s)   :",
    round(total_time, 6),
)

print(
    "Average (ms)     :",
    round(average * 1000, 3),
)

print(
    "Minimum (ms)     :",
    round(minimum * 1000, 3),
)

print(
    "Maximum (ms)     :",
    round(maximum * 1000, 3),
)

print(
    "Throughput/sec   :",
    round(throughput, 2),
)

assert len(handled) == TOTAL_EVENTS

assert throughput > 0

print()

print("=" * 60)
print("PERFORMANCE TEST PASSED")
print("=" * 60)
