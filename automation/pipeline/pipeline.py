from __future__ import annotations

from automation.pipeline.pipeline_stage import (
    PipelineStage,
)


class EventPipeline:
    """
    Executes an event through
    multiple pipeline stages.
    """

    def __init__(self):

        self._stages = []

    # -------------------------------- #

    def add_stage(
        self,
        stage: PipelineStage,
    ):

        self._stages.append(
            stage
        )

        return stage

    # -------------------------------- #

    def remove_stage(
        self,
        stage: PipelineStage,
    ):

        if stage in self._stages:

            self._stages.remove(
                stage
            )

            return True

        return False

    # -------------------------------- #

    def clear(self):

        self._stages.clear()

    # -------------------------------- #

    def process(
        self,
        event,
    ):

        current = event

        for stage in self._stages:

            if current is None:

                break

            current = stage(
                current
            )

        return current

    # -------------------------------- #

    def count(self):

        return len(
            self._stages
        )

    # -------------------------------- #

    def __len__(self):

        return self.count()

    # -------------------------------- #

    def __iter__(self):

        return iter(
            self._stages
        )

    # -------------------------------- #

    def __repr__(self):

        return (
            "<EventPipeline "
            f"stages={self.count()}>"
        )
