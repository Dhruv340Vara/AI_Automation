from __future__ import annotations

import time

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

print("=" * 60)
print("          RUNTIME VALIDATION")
print("=" * 60)


# =====================================================
# Pipeline Stage
# =====================================================

class ValidationStage(
    PipelineStage,
):

    def process(
        self,
        event,
    ):

        event.payload[
            "validated"
        ] = True

        return event


# =====================================================
# Runtime
# =====================================================

runtime = AutomationRuntime()

handled = []


def handler(event):

    handled.append(event)


runtime.event_registry.register(

    EventType.MANUAL,

    handler,

)


runtime.add_condition(

    ComparisonCondition(

        name="Battery",

        key="battery",

        operator_symbol="<",

        expected=20,

    )

)

runtime.add_pipeline_stage(

    ValidationStage(
        "Validation"
    )

)

# =====================================================
# Start
# =====================================================

print()

print("Starting Runtime...")

assert runtime.start()

assert runtime.scheduler.is_running

print("PASS")

# =====================================================
# Events
# =====================================================

print()

print("Sending Events...")

TOTAL = 5

for i in range(TOTAL):

    event = Event(

        event_type=EventType.MANUAL,

        source="runtime",

        payload={

            "battery": 10,

            "index": i,

        },

    )

    assert runtime.emit_event(
        event
    )

    assert event.payload[
        "validated"
    ]

time.sleep(0.2)

assert len(
    handled
) == TOTAL

print("PASS")

# =====================================================
# Stop
# =====================================================

print()

print("Stopping Runtime...")

assert runtime.stop()

assert not runtime.scheduler.is_running

print("PASS")

# =====================================================
# Restart
# =====================================================

print()

print("Restarting Runtime...")

assert runtime.start()

assert runtime.scheduler.is_running

assert runtime.stop()

print("PASS")

# =====================================================

print()

print("Handled Events :", len(handled))

print()

print("=" * 60)

print("RUNTIME VALIDATION PASSED")

print("=" * 60)
