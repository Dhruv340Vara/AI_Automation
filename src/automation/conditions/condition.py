from __future__ import annotations

from abc import ABC, abstractmethod


class Condition(ABC):
    """
    Base class for all conditions.
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
    def evaluate(
        self,
        context: dict,
    ) -> bool:
        """
        Evaluate the condition.
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
        context: dict,
    ) -> bool:

        if not self.enabled:
            return False

        return self.evaluate(
            context
        )

    # -------------------------------- #

    def __repr__(self):

        state = (
            "enabled"
            if self.enabled
            else "disabled"
        )

        return (
            "<Condition "
            f"{self.name} "
            f"({state})>"
        )
