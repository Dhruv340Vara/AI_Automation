from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from typing import Any


class Tool(ABC):
    """
    Base class for every AI tool.
    """

    def __init__(
        self,
        name: str,
        description: str = "",
        enabled: bool = True,
    ):

        self.name = name

        self.description = description

        self.enabled = enabled

    # -------------------------------- #

    def enable(self):

        self.enabled = True

    # -------------------------------- #

    def disable(self):

        self.enabled = False

    # -------------------------------- #

    def is_enabled(
        self,
    ):

        return self.enabled

    # -------------------------------- #

    @abstractmethod
    def execute(
        self,
        **kwargs: Any,
    ):
        """
        Execute the tool.
        """

        raise NotImplementedError

    # -------------------------------- #

    def __repr__(self):

        status = (
            "enabled"
            if self.enabled
            else "disabled"
        )

        return (
            f"<Tool "
            f"{self.name} "
            f"({status})>"
        )
