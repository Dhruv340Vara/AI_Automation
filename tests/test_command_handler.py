from automation.assistant.command import (
    Command,
)

from automation.assistant.handlers import (
    CommandHandler,
)


class DemoHandler(
    CommandHandler,
):

    def __init__(self):

        super().__init__(
            "Demo",
        )

    def execute(
        self,
        command,
    ):

        print(

            "Hello",

            command.get_parameter(
                "name"
            ),

        )


handler = DemoHandler()

print(handler)

print()

print(

    handler.is_enabled()

)

print()

command = Command(

    name="demo",

)

command.set_parameter(

    "name",

    "Dhruv",

)

handler.execute(
    command
)

print()

handler.disable()

print(handler)

print()

handler.enable()

print(handler)

print()

print(

    handler.validate(
        command
    )

)
