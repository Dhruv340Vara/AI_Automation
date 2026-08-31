from automation.devices import (
    DeviceRequest,
)

from automation.devices.actions import (
    DeviceAction,
    DeviceActionRegistry,
)


class DemoAction(DeviceAction):

    def __init__(self):

        super().__init__(
            "demo",
        )

    def perform(
        self,
        request,
    ):

        print()

        print(
            "Executing Device Action"
        )

        print(
            request.action
        )

        print(
            request.parameters
        )

        return True


registry = DeviceActionRegistry()

print(registry)

print()

action = DemoAction()

registry.register(
    action,
)

print(
    registry.count()
)

print()

print(
    registry.actions()
)

print()

print(
    registry.exists(
        "demo"
    )
)

print()

request = DeviceRequest(
    action="demo",
)

request.set_parameter(
    "name",
    "Dhruv",
)

print(
    registry.execute(
        request
    )
)

print()

registry.unregister(
    "demo",
)

print(
    registry.actions()
)

print()

print(registry)
