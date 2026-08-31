"""
command_handler.py

Base class for all assistant command handlers.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from automation.assistant.command import (
    Command,
)


class CommandHandler(ABC):

    def __init__(
        self,
        name: str,
    ):

        self.name = name

        self.enabled = True

    # -------------------------------- #

    @abstractmethod
    def execute(
        self,
        command: Command,
    ):
        """
        Execute the command.
        """

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

    def validate(
        self,
        command: Command,
    ):

        return True

    # -------------------------------- #

    def __repr__(self):

        state = (

            "enabled"

            if self.enabled

            else "disabled"

        )

        return (

            f"<Handler "

            f"{self.name} "

            f"({state})>"

        )
