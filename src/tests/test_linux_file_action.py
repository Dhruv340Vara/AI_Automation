from automation.devices import (
    DeviceRequest,
)

from automation.devices.actions.linux import (
    LinuxFileAction,
)

action = LinuxFileAction()

print(action)

print()

# ---------------------------- #
# CREATE FOLDER

req1 = DeviceRequest(action="file")
req1.set_parameter("operation", "mkdir")
req1.set_parameter("path", "TestFolder")

print("Create Folder")
print(action.execute(req1))

print()

# ---------------------------- #
# COPY

req2 = DeviceRequest(action="file")
req2.set_parameter("operation", "copy")
req2.set_parameter("path", "TestFolder")
req2.set_parameter("target", "TestFolder_Copy")

print("Copy Folder")
print(action.execute(req2))

print()

# ---------------------------- #
# RENAME

req3 = DeviceRequest(action="file")
req3.set_parameter("operation", "rename")
req3.set_parameter("path", "TestFolder_Copy")
req3.set_parameter("target", "RenamedFolder")

print("Rename Folder")
print(action.execute(req3))

print()

# ---------------------------- #
# DELETE

req4 = DeviceRequest(action="file")
req4.set_parameter("operation", "delete")
req4.set_parameter("path", "TestFolder")

print("Delete Folder")
print(action.execute(req4))

print()

# ---------------------------- #
# INVALID

req5 = DeviceRequest(action="file")
req5.set_parameter("operation", "invalid")

try:
    action.execute(req5)
except Exception as e:
    print(e)
