from automation.pipeline.pipeline import (
    EventPipeline,
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


class StageOne(
    PipelineStage,
):

    def process(
        self,
        event,
    ):

        event.payload[
            "stage1"
        ] = True

        return event


class StageTwo(
    PipelineStage,
):

    def process(
        self,
        event,
    ):

        event.payload[
            "stage2"
        ] = True

        return event


pipeline = EventPipeline()

pipeline.add_stage(
    StageOne(
        "Stage One"
    )
)

pipeline.add_stage(
    StageTwo(
        "Stage Two"
    )
)

print(pipeline)

event = Event(

    event_type=EventType.MANUAL,

    source="test",

    payload={},

)

event = pipeline.process(
    event
)

print(event.payload)

print(len(pipeline))
