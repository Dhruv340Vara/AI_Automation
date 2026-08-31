from automation.triggers.trigger import Trigger

from automation.triggers.trigger_types import (
    TriggerType,
)

from automation.triggers.trigger_registry import (
    TriggerRegistry,
)


def run():

    registry = TriggerRegistry()

    trigger = Trigger(

        trigger_type=TriggerType.TIME,

        name="Morning Trigger",

    )

    registry.register(trigger)

    print(registry)

    print(registry.count())

    print(
        registry.exists(
            trigger.trigger_id
        )
    )

    print(
        registry.get(
            trigger.trigger_id
        )
    )

    print(
        registry.enabled()
    )

    trigger.disable()

    print(
        registry.disabled()
    )

    registry.unregister(
        trigger.trigger_id
    )

    print(registry.count())


if __name__ == "__main__":

    run()
