from __future__ import annotations

import time

print("=" * 60)
print("          MASTER INTEGRATION TEST")
print("=" * 60)

from automation.automation_runtime import (
    AutomationRuntime,
)

from automation.events.event import (
    Event,
)

from automation.events.event_types import (
    EventType,
)

from automation.conditions.comparison_condition import (
    ComparisonCondition,
)

from automation.pipeline.pipeline_stage import (
    PipelineStage,
)


# ==========================================================
# Pipeline Stage
# ==========================================================

class ValidationStage(PipelineStage):

    def process(
        self,
        event,
    ):

        event.payload[
            "validated"
        ] = True

        return event


class LoggingStage(PipelineStage):

    def process(
        self,
        event,
    ):

        event.payload[
            "logged"
        ] = True

        return event


# ==========================================================
# Runtime
# ==========================================================

runtime = AutomationRuntime()

handled = []


def handler(event):

    handled.append(event)

    print(
        "[Handler]",
        event.event_type.value,
    )

    print(
        event.payload,
    )


runtime.event_registry.register(

    EventType.MANUAL,

    handler,

)


# ==========================================================
# Condition
# ==========================================================

condition = ComparisonCondition(

    name="Battery",

    key="battery",

    operator_symbol="<",

    expected=20,

)

runtime.add_condition(
    condition
)


# ==========================================================
# Pipeline
# ==========================================================

runtime.add_pipeline_stage(

    ValidationStage(
        "Validation"
    )

)

runtime.add_pipeline_stage(

    LoggingStage(
        "Logging"
    )

)


# ==========================================================
# Runtime
# ==========================================================

runtime.start()

print("\nRuntime Started")


event = Event(

    event_type=EventType.MANUAL,

    source="master",

    payload={

        "battery": 10,

    },

)

assert runtime.emit_event(
    event
)

time.sleep(0.2)

runtime.stop()

# ==========================================================
# Assertions
# ==========================================================

assert len(
    handled
) == 1

assert event.payload[
    "validated"
]

assert event.payload[
    "logged"
]

assert handled[
    0
].payload[
    "battery"
] == 10

print()

print("All Assertions Passed")

print(
    "Handled Events:",
    len(handled),
)

print()

print("=" * 60)
print("MASTER INTEGRATION TEST PASSED")
print("=" * 60)
