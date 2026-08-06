"""
Device Layer Test Suite
"""

from automation.devices import (
    DeviceManager,
    DeviceRequest,
    LinuxDevice,
    AndroidDevice,
)

print("=" * 60)
print("             DEVICE TEST SUITE")
print("=" * 60)
print()

# ------------------------------------------------ #

print("Creating Device Manager...")

manager = DeviceManager()

print("PASS")
print()

# ------------------------------------------------ #

print("Registering Devices...")

linux = LinuxDevice()

android = AndroidDevice()

manager.register(
    linux,
)

manager.register(
    android,
)

assert manager.count() == 2

print(manager.devices())

print("PASS")
print()

# ------------------------------------------------ #

print("Testing Linux Device...")

request = DeviceRequest(
    action="torch",
)

request.set_parameter(
    "state",
    "on",
)

assert manager.execute(
    "linux",
    request,
)

print("PASS")
print()

# ------------------------------------------------ #

print("Testing Android Device...")

request = DeviceRequest(
    action="call",
)

request.set_parameter(
    "contact",
    "Mummy",
)

assert manager.execute(
    "android",
    request,
)

print("PASS")
print()

# ------------------------------------------------ #

print("Testing Disabled Device...")

linux.disable()

try:

    manager.execute(
        "linux",
        request,
    )

except Exception as error:

    print(error)

print("PASS")
print()

# ------------------------------------------------ #

print("Testing Unknown Device...")

try:

    manager.execute(
        "windows",
        request,
    )

except Exception as error:

    print(error)

print("PASS")
print()

# ------------------------------------------------ #

print("Registered Devices:")

print(
    manager.devices()
)

print()

print("=" * 60)
print("ALL DEVICE TESTS PASSED")
print("=" * 60)

