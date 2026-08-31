from automation.assistant.command import (
    Command,
    CommandStatus,
)

command = Command(
    name="Call",
    description="Call Mummy",
)

print(command)

print()

command.set_parameter(
    "contact",
    "Mummy",
)

command.set_parameter(
    "number",
    "9876543210",
)

print(command.to_dict())

print()

command.start()

print(command.status)

command.complete()

print(command.status)

print(command.is_completed())

print()

copy = Command.from_dict(
    command.to_dict()
)

print(copy)

print()

print(
    copy.get_parameter(
        "contact"
    )
)
