"""
torch_handler.py

Handles flashlight commands.
"""

from __future__ import annotations

from automation.assistant.command import Command

from automation.assistant.handlers.device_command_handler import (
    DeviceCommandHandler,
)


class TorchHandler(DeviceCommandHandler):

    def __init__(self):

        super().__init__("Torch")

    # ---------------------------- #

    def validate(
        self,
        command: Command,
    ):

        state = command.get_parameter(
            "state"
        )

        return state in (

            "on",

            "off",

            "toggle",

        )

    # ---------------------------- #

    def perform(
        self,
        command: Command,
    ):

        state = command.get_parameter(
            "state"
        )

        print()

        print("TORCH REQUEST")

        print(

            "State :",

            state.upper(),

        )

        print()

        print(

            "Waiting for Device Layer..."

        )

        return True
