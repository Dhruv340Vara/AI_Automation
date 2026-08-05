from automation.automation_runtime import (
    AutomationRuntime,
)

from automation.pipeline.pipeline_stage import (
    PipelineStage,
)

from automation.events.event import (
    Event,
)

from automation.events.event_types import (
    EventType,
)


class DemoStage(
    PipelineStage,
):

    def process(
        self,
        event,
    ):

        event.payload[
            "pipeline"
        ] = True

        return event


runtime = AutomationRuntime()

runtime.add_pipeline_stage(
    DemoStage(
        "Demo"
    )
)

runtime.start()

event = Event(

    event_type=EventType.MANUAL,

    source="test",

    payload={},

)

runtime.emit_event(
    event
)

runtime.stop()

print(event.payload)
