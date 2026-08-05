from __future__ import annotations

import time

from automation.automation_runtime import (
    AutomationRuntime,
)

from automation.events.event_types import (
    EventType,
)

from automation.triggers.api_trigger import (
    APITrigger,
)

print("=" * 60)
print("            API TEST SUITE")
print("=" * 60)

runtime = AutomationRuntime()

handled_events = []


def api_handler(event):

    handled_events.append(event)

    print(
        "[Handler]",
        event.event_type.value,
    )

    print(
        event.payload,
    )


runtime.event_registry.register(
    EventType.API,
    api_handler,
)

trigger = APITrigger(

    name="HTTPBin",

    url="https://httpbin.org/get",

    interval=2,

)

runtime.register_api_trigger(
    trigger
)

runtime.start()

print("\nRuntime Started")

timeout = time.time() + 8

while (
    len(handled_events) == 0
    and time.time() < timeout
):

    time.sleep(0.2)

runtime.stop()

assert len(
    handled_events
) >= 1

event = handled_events[0]

assert (
    event.event_type
    == EventType.API
)

assert (
    "url"
    in event.payload
)

assert (
    event.payload["url"]
    == "https://httpbin.org/get"
)

assert (
    "method"
    in event.payload
)

assert (
    event.payload["method"]
    == "GET"
)

print()

print("All Assertions Passed")

print(
    "Events Received:",
    len(handled_events),
)

print(
    "Status Code:",
    event.payload.get(
        "status_code"
    )
)

print()

print("=" * 60)

print("API TEST SUITE PASSED")

print("=" * 60)
