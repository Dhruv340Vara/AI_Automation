from automation.devices import (
    Device,
    DeviceManager,
    DeviceRequest,
)


class DemoDevice(Device):

    def __init__(self):

        super().__init__(
            "Linux",
        )

    def execute(
        self,
        request,
    ):

        print()

        print("Executing")

        print(request.action)

        print(request.parameters)

        return True


manager = DeviceManager()

print(manager)

print()

device = DemoDevice()

manager.register(
    device,
)

print(manager)

print()

print(
    manager.devices()
)

print()

request = DeviceRequest(
    action="torch",
)

request.set_parameter(
    "state",
    "on",
)

print(

    manager.execute(

        "linux",

        request,

    )

)

print()

device.disable()

try:

    manager.execute(

        "linux",

        request,

    )

except Exception as error:

    print(error)

print()

manager.unregister(
    "linux",
)

print(manager)
