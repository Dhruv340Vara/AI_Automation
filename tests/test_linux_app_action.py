from automation.devices import (
    DeviceRequest,
)

from automation.devices.actions.linux import (
    LinuxAppAction,
)


action = LinuxAppAction()

print(action)

print()

request = DeviceRequest(
    action="open_app",
)

request.set_parameter(
    "app",
    "firefox",
)

print(
    action.execute(
        request,
    )
)

print()

invalid = DeviceRequest(
    action="open_app",
)

invalid.set_parameter(
    "app",
    "xyz_unknown_app",
)

try:

    action.execute(
        invalid,
    )

except Exception as error:

    print(error)
