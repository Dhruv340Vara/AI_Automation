from automation.assistant.command import (
    Command,
)

from automation.assistant.command_executor import (
    CommandExecutor,
)


def call_handler(command):

    print(

        "Calling",

        command.get_parameter(

            "contact"

        ),

    )


executor = CommandExecutor()

print(executor)

print()

command = Command(

    name="call",

)

command.set_parameter(

    "contact",

    "Mummy",

)

success = executor.execute(

    command,

    call_handler,

)

print()

print(success)

print()

print(command.status)

print()

print(command.is_completed())

print()

print(executor.count())

print()

failed = Command(

    name="unknown",

)

print(

    executor.execute(

        failed,

        None,

    )

)

print()

print(failed.status)

print()

print(executor)
