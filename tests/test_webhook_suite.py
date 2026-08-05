from __future__ import annotations

import time

from automation.automation_runtime import (
    AutomationRuntime,
)

from automation.events.event_types import (
    EventType,
)

from automation.triggers.webhook_trigger import (
    WebhookTrigger,
)

print("=" * 60)
print("          WEBHOOK TEST SUITE")
print("=" * 60)

runtime = AutomationRuntime()

handled_events = []


def webhook_handler(event):

    handled_events.append(event)

    print(
        "[Handler]",
        event.event_type.value,
    )

    print(
        event.payload,
    )


runtime.event_registry.register(

    EventType.WEBHOOK,

    webhook_handler,

)

trigger = WebhookTrigger(

    name="GitHub",

    endpoint="/github",

    methods=["POST"],

    secret="12345",

)

runtime.register_webhook_trigger(
    trigger
)

runtime.start()

print("\nRuntime Started")

runtime.emit_webhook(

    endpoint="/github",

    method="POST",

    headers={
        "X-Webhook-Secret": "12345",
    },

    body={
        "repository": "AI_Automation",
        "branch": "main",
        "event": "push",
    },

)

time.sleep(1)

runtime.stop()

assert len(
    handled_events
) == 1

event = handled_events[0]

assert (
    event.event_type
    == EventType.WEBHOOK
)

assert (
    event.payload["endpoint"]
    == "/github"
)

assert (
    event.payload["body"]["event"]
    == "push"
)

print()

print("All Assertions Passed")

print(
    "Handled Events:",
    len(handled_events),
)

print()

print("=" * 60)

print("WEBHOOK TEST SUITE PASSED")

print("=" * 60)
