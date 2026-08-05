from automation.automation_runtime import (
    AutomationRuntime,
)

from automation.events.event_types import (
    EventType,
)

from automation.triggers.webhook_trigger import (
    WebhookTrigger,
)

runtime = AutomationRuntime()


def handler(event):

    print(
        event.event_type.value,
        event.payload,
    )


runtime.event_registry.register(

    EventType.WEBHOOK,

    handler,

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

runtime.emit_webhook(

    endpoint="/github",

    headers={
        "X-Webhook-Secret": "12345",
    },

    body={
        "repository": "AI_Automation",
        "action": "push",
    },

)

runtime.stop()

print("Webhook Runtime OK")
