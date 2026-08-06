from automation.triggers.api_trigger import (
    APITrigger,
)

trigger = APITrigger(
    name="Weather API",
    url="https://api.weather.com/v1",
    interval=300,
    headers={
        "Authorization": "Bearer TOKEN",
    },
    params={
        "city": "Ahmedabad",
    },
)

print(trigger)

print(trigger.url)

print(trigger.method)

print(trigger.interval)

print(trigger.headers)

print(trigger.params)

print(trigger.is_get())

print(trigger.is_post())
