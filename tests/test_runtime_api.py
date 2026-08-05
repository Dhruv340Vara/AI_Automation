import time

from automation.automation_runtime import (
    AutomationRuntime,
)

from automation.events.event_types import (
    EventType,
)

from automation.triggers.api_trigger import (
    APITrigger,
)

runtime = AutomationRuntime()


def handler(event):

    print(
        event.event_type.value
    )

    print(
        event.payload["status_code"]
    )


runtime.event_registry.register(

    EventType.API,

    handler,

)

trigger = APITrigger(

    name="HTTPBin",

    url="https://httpbin.org/get",

    interval=2,

)

runtime.register_api_trigger(
    trigger
)

runtime.start()

time.sleep(5)

runtime.stop()

print("Runtime API OK")
