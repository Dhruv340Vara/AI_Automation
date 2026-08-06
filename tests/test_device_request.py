from automation.devices import (
    DeviceRequest,
)

request = DeviceRequest(
    action="torch",
)

print(request)

print()

request.set_parameter(
    "state",
    "on",
)

request.set_metadata(
    "source",
    "voice",
)

print(

    request.to_dict()

)

print()

copy = DeviceRequest.from_dict(

    request.to_dict()

)

print(copy)

print()

print(

    copy.get_parameter(
        "state"
    )

)

print(

    copy.get_metadata(
        "source"
    )

)
