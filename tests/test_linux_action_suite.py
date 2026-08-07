from automation.devices.actions.linux import (
    LinuxActionSuite,
)

from automation.devices import (
    DeviceRequest,
)


suite = LinuxActionSuite()

print(suite)

print()

print("Available Actions:")
print(suite.list_actions())

print()

registry = suite.get_registry()

# ---------------------------- #
# TEST APP

req1 = DeviceRequest(action="open_app")
req1.set_parameter("app", "firefox")

print("Open App:")
print(registry.execute(req1))
print()

# ---------------------------- #
# TEST SHELL

req2 = DeviceRequest(action="shell")
req2.set_parameter("command", ["pwd"])

print("Shell:")
print(registry.execute(req2))
print()

# ---------------------------- #
# TEST FILE

req3 = DeviceRequest(action="file")
req3.set_parameter("operation", "mkdir")
req3.set_parameter("path", "SuiteTest")

print("File:")
print(registry.execute(req3))
print()
