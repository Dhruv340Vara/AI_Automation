from automation.triggers.trigger import Trigger

from automation.triggers.trigger_types import (
    TriggerType,
)


def run():

    trigger = Trigger(

        trigger_type=TriggerType.TIME,

        name="Morning Trigger",

    )

    print(trigger)

    trigger.disable()

    print(trigger.enabled)

    trigger.enable()

    print(trigger.enabled)

    data = trigger.to_dict()

    loaded = Trigger.from_dict(data)

    print(loaded)


if __name__ == "__main__":

    run()
