from automation.devices import (
    AndroidDevice,
    DeviceRequest,
)

device = AndroidDevice()

print(device)

print()

request = DeviceRequest(
    action="call",
)

request.set_parameter(
    "contact",
    "Mummy",
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
