"""
device_command_handler.py

Base handler for device-related commands.
"""

from __future__ import annotations

from abc import abstractmethod

from automation.assistant.command import (
    Command,
)

from automation.assistant.handlers.command_handler import (
    CommandHandler,
)


class DeviceCommandHandler(CommandHandler):

    def __init__(
        self,
        name: str,
    ):

        super().__init__(name)

    # -------------------------------- #

    def validate(
        self,
        command: Command,
    ):

        return True

    # -------------------------------- #

    def execute(
        self,
        command: Command,
    ):

        if not self.is_enabled():

            raise RuntimeError(
                f"{self.name} handler is disabled."
            )

        if not self.validate(command):

            raise ValueError(
                "Invalid command."
            )

        return self.perform(
            command
        )

    # -------------------------------- #

    @abstractmethod
    def perform(
        self,
        command: Command,
    ):
        """
        Device specific work.
        """

    # -------------------------------- #

    def __repr__(self):

        state = (

            "enabled"

            if self.enabled

            else "disabled"

        )

        return (

            f"<{self.__class__.__name__} "

            f"{state}>"

        )
