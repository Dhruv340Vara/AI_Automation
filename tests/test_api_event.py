from automation.events.api_event import (
    APIEventFactory,
)

event = APIEventFactory.response(
    url="https://api.weather.com",
    method="GET",
    status_code=200,
    response={
        "temperature": 31,
        "condition": "Sunny",
    },
)

print(event)

print(event.event_type.value)

print(event.payload)

print("-" * 50)

event = APIEventFactory.error(
    url="https://api.weather.com",
    method="GET",
    error="Connection Error",
)

print(event.payload)

print("-" * 50)

event = APIEventFactory.timeout(
    url="https://api.weather.com",
    timeout=30,
)

print(event.payload)
