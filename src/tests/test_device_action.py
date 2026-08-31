from automation.devices import (
    DeviceRequest,
)

from automation.devices.actions import (
    DeviceAction,
)


class DemoAction(DeviceAction):

    def __init__(self):

        super().__init__(
            "Demo",
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


action = DemoAction()

print(action)

print()

request = DeviceRequest(
    action="demo",
)

request.set_parameter(
    "name",
    "Dhruv",
)

print(
    action.execute(
        request
    )
)

print()

action.disable()

print(action)

print()

try:

    action.execute(
        request
    )

except Exception as error:

    print(error)
