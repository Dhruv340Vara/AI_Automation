from automation.automation_runtime import (
    AutomationRuntime,
)

from automation.events.event_types import (
    EventType,
)

from automation.manual import (
    ManualTriggerManager,
)

from automation.triggers.manual_trigger import (
    ManualTrigger,
)

runtime = AutomationRuntime()

manager = ManualTriggerManager(
    runtime,
)


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

)

manager.register(
    trigger
)

runtime.start()

manager.trigger(

    "Backup",

    user="Dhruv",

)

runtime.stop()

print(manager)
