from automation.devices import (
    DeviceRequest,
)

from automation.devices.actions.linux import (
    LinuxShellAction,
)


action = LinuxShellAction()

print(action)

print()

# ---------------------------- #

print("PWD")

req1 = DeviceRequest(
    action="shell",
)

req1.set_parameter(
    "command",
    ["pwd"],
)

print(
    action.execute(
        req1
    )
)

print()

# ---------------------------- #

print("LS")

req2 = DeviceRequest(
    action="shell",
)

req2.set_parameter(
    "command",
    "ls",
)

print(
    action.execute(
        req2
    )
)

print()

# ---------------------------- #

print("INVALID")

req3 = DeviceRequest(
    action="shell",
)

req3.set_parameter(
    "command",
    "xyz_unknown_command",
)

try:

    action.execute(
        req3
    )

except Exception as error:

    print(error)
