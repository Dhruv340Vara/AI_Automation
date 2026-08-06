from automation.devices import (
    Device,
    DeviceRequest,
)


class DemoDevice(Device):

    def __init__(self):

        super().__init__(
            "Demo",
        )

    def execute(
        self,
        request,
    ):

        print()

        print(
            "Executing Device Request"
        )

        print(
            request.action
        )

        print(
            request.parameters
        )

        return True


device = DemoDevice()

print(device)

print()

print(
    device.is_enabled()
)

print()

request = DeviceRequest(
    action="torch",
)

request.set_parameter(
    "state",
    "on",
)

device.execute(
    request,
)

print()

device.disable()

print(device)

print()

print(
    device.is_enabled()
)

device.enable()

print()

print(device)
