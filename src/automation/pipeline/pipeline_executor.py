from __future__ import annotations

from automation.pipeline.pipeline import (
    EventPipeline,
)


class PipelineExecutor:
    """
    Executes an EventPipeline.
    """

    def __init__(
        self,
        pipeline: EventPipeline,
    ):

        self.pipeline = pipeline

        self._executed = 0

    # ---------------------------- #

    @property
    def executed(self):

        return self._executed

    # ---------------------------- #

    def execute(
        self,
        event,
    ):

        result = self.pipeline.process(
            event
        )

        if result is not None:

            self._executed += 1

        return result

    # ---------------------------- #

    def reset(self):

        self._executed = 0

    # ---------------------------- #

    def __repr__(self):

        return (
            "<PipelineExecutor "
            f"executed={self.executed}>"
        )
