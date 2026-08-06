from automation.assistant.command import (
    Command,
)

from automation.assistant.handlers.call_handler import (
    CallHandler,
)

handler = CallHandler()

print(handler)

print()

command = Command(

    name="call",

)

command.set_parameter(

    "contact",

    "Mummy",

)

command.set_parameter(

    "number",

    "9876543210",

)

print(

    handler.validate(

        command,

    )

)

print()

handler.execute(

    command,

)

print()

handler.disable()

print(handler)

print()

try:

    handler.execute(
        command,
    )

except Exception as e:

    print(e)

print()

invalid = Command(

    name="call",

)

print(

    handler.validate(

        invalid,

    )

)
