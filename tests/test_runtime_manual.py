from automation.automation_runtime import (
    AutomationRuntime,
)

from automation.events.event_types import (
    EventType,
)

from automation.triggers.manual_trigger import (
    ManualTrigger,
)

runtime = AutomationRuntime()


def handler(event):

    print(
        event.event_type.value
    )

    print(
        event.payload
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

runtime.trigger_manual(
    "Backup",
    user="Dhruv",
)

runtime.stop()

print("Runtime Manual OK")
