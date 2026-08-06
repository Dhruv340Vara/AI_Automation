from __future__ import annotations

from automation.assistant.command import (
    Command,
)

from automation.assistant.handlers.command_handler import (
    CommandHandler,
)


class CallHandler(CommandHandler):

    def __init__(self):

        super().__init__(
            "Call",
        )

    # ---------------------------- #

    def validate(

        self,

        command: Command,

    ):

        contact = command.get_parameter(
            "contact"
        )

        number = command.get_parameter(
            "number"
        )

        return bool(
            contact or number
        )

    # ---------------------------- #

    def execute(

        self,

        command: Command,

    ):

        if not self.is_enabled():

            raise RuntimeError(
                "Call handler is disabled."
            )

        if not self.validate(
            command,
        ):

            raise ValueError(
                "Missing contact or number."
            )

        contact = command.get_parameter(
            "contact",
        )

        number = command.get_parameter(
            "number",
        )

        print()

        print("CALL REQUEST")

        print(
            "Contact :",
            contact,
        )

        print(
            "Number  :",
            number,
        )

        print()

        print(
            "Waiting for Device Layer..."
        )

        return True

    # ---------------------------- #

    def __repr__(self):

        state = (

            "enabled"

            if self.enabled

            else "disabled"

        )

        return (

            f"<CallHandler "

            f"{state}>"

        )
