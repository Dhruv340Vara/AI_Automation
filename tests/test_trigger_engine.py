from automation.triggers.trigger import Trigger

from automation.triggers.trigger_engine import (
    TriggerEngine,
)

from automation.triggers.trigger_types import (
    TriggerType,
)


def run():

    engine = TriggerEngine(

        "data/test_triggers.json"

    )

    engine.registry.clear()

    trigger = Trigger(

        TriggerType.TIME,

        "Morning Trigger",

    )

    engine.register(trigger)

    print(engine.count())

    print(engine.enabled())

    engine2 = TriggerEngine(

        "data/test_triggers.json"

    )

    print(engine2.count())

    print(engine2.all())


if __name__ == "__main__":

    run()
