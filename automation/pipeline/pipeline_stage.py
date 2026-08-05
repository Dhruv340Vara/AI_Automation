from __future__ import annotations

from abc import ABC, abstractmethod


class PipelineStage(ABC):
    """
    Base class for all pipeline stages.
    """

    def __init__(
        self,
        name: str,
        enabled: bool = True,
    ):

        self.name = name

        self.enabled = enabled

    # -------------------------------- #

    @abstractmethod
    def process(
        self,
        event,
    ):
        """
        Process an event and return it.
        Returning None stops the pipeline.
        """
        raise NotImplementedError

    # -------------------------------- #

    def enable(self):

        self.enabled = True

    # -------------------------------- #

    def disable(self):

        self.enabled = False

    # -------------------------------- #

    def is_enabled(self):

        return self.enabled

    # -------------------------------- #

    def __call__(
        self,
        event,
    ):

        if not self.enabled:
            return event

        return self.process(
            event
        )

    # -------------------------------- #

    def __repr__(self):

        state = (
            "enabled"
            if self.enabled
            else "disabled"
        )

        return (
            "<PipelineStage "
            f"{self.name} "
            f"({state})>"
        )
