from automation.assistant.command import (
    Command,
)

from automation.assistant.handlers.device_command_handler import (
    DeviceCommandHandler,
)


class DemoDeviceHandler(
    DeviceCommandHandler,
):

    def __init__(self):

        super().__init__(
            "Demo Device"
        )

    def perform(
        self,
        command,
    ):

        print(

            "Executing Device Command"

        )

        print(

            command.parameters

        )

        return True


handler = DemoDeviceHandler()

print(handler)

print()

command = Command(
    name="device"
)

command.set_parameter(
    "state",
    "on"
)

print(
    handler.execute(command)
)

print()

handler.disable()

print(handler)

print()

try:

    handler.execute(command)

except Exception as e:

    print(e)
