from automation.pipeline.pipeline import (
    EventPipeline,
)

from automation.pipeline.pipeline_executor import (
    PipelineExecutor,
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

executor = PipelineExecutor(
    pipeline
)

event = Event(

    event_type=EventType.MANUAL,

    source="test",

    payload={},

)

result = executor.execute(
    event
)

print(executor)

print(result.payload)

print(executor.executed)

executor.reset()

print(executor.executed)
