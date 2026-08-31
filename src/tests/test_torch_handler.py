from automation.assistant.command import (
    Command,
)

from automation.assistant.handlers import (
    TorchHandler,
)


handler = TorchHandler()

print(handler)

print()

command = Command(

    name="torch",

)

command.set_parameter(

    "state",

    "on",

)

print(

    handler.validate(

        command

    )

)

print()

print(

    handler.execute(

        command

    )

)

print()

handler.disable()

print(handler)

print()

try:

    handler.execute(

        command

    )

except Exception as error:

    print(error)

print()

invalid = Command(

    name="torch",

)

invalid.set_parameter(

    "state",

    "hello",

)

print(

    handler.validate(

        invalid

    )

)
