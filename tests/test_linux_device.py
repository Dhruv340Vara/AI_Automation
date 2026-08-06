from automation.devices import (
    DeviceRequest,
    LinuxDevice,
)

device = LinuxDevice()

print(device)

print()

request = DeviceRequest(
    action="torch",
)

request.set_parameter(
    "state",
    "on",
)

print(
    device.supports(
        request
    )
)

print()

print(
    device.execute(
        request
    )
)

print()

device.disable()

print(device)

print()

try:

    device.execute(
        request
    )

except Exception as e:

    print(e)
