from __future__ import annotations

print("=" * 60)
print("           PIPELINE TEST SUITE")
print("=" * 60)

from automation.pipeline.pipeline import (
    EventPipeline,
)

from automation.pipeline.pipeline_executor import (
    PipelineExecutor,
)

from automation.pipeline.pipeline_stage import (
    PipelineStage,
)

from automation.automation_runtime import (
    AutomationRuntime,
)

from automation.events.event import (
    Event,
)

from automation.events.event_types import (
    EventType,
)

# ------------------------------------------------


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


# ------------------------------------------------

pipeline = EventPipeline()

pipeline.add_stage(
    ValidationStage(
        "Validation"
    )
)

pipeline.add_stage(
    LoggingStage(
        "Logging"
    )
)

executor = PipelineExecutor(
    pipeline
)

event = Event(

    event_type=EventType.MANUAL,

    source="pipeline",

    payload={},

)

print("\nPipeline")

result = executor.execute(
    event
)

assert result is not None

assert (
    result.payload[
        "validated"
    ]
)

assert (
    result.payload[
        "logged"
    ]
)

print("PASS")

print(result.payload)

# ------------------------------------------------

runtime = AutomationRuntime()

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

runtime.start()

event = Event(

    event_type=EventType.MANUAL,

    source="runtime",

    payload={},

)

print("\nRuntime")

assert runtime.emit_event(
    event
)

runtime.stop()

assert (
    event.payload[
        "validated"
    ]
)

assert (
    event.payload[
        "logged"
    ]
)

print("PASS")

print(event.payload)

# ------------------------------------------------

print()

print("Stages Executed:")

print(
    executor.executed
)

print()

print("=" * 60)

print("PIPELINE TEST SUITE PASSED")

print("=" * 60)
