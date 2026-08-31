from automation.automation_runtime import (
    AutomationRuntime,
)

from automation.conditions.comparison_condition import (
    ComparisonCondition,
)

from automation.events import (
    Event,
    EventType,
)

runtime = AutomationRuntime()

condition = ComparisonCondition(

    name="Battery",

    key="battery",

    operator_symbol="<",

    expected=20,

)

runtime.add_condition(
    condition
)

runtime.start()

event = Event(

    event_type=EventType.MANUAL,

    source="test",

    payload={

        "battery": 10,

    },

)

print(

    runtime.emit_event(
        event
    )

)

event = Event(

    event_type=EventType.MANUAL,

    source="test",

    payload={

        "battery": 80,

    },

)

print(

    runtime.emit_event(
        event
    )

)

runtime.stop()

print("Condition Runtime OK")
