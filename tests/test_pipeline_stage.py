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
            "processed"
        ] = True

        return event


stage = DemoStage(
    "Demo Stage"
)

print(stage)

event = Event(

    event_type=EventType.MANUAL,

    source="test",

    payload={},

)

event = stage(
    event
)

print(event.payload)

stage.disable()

print(stage.is_enabled())

event = stage(
    event
)

print(event.payload)

stage.enable()

print(stage.is_enabled())
