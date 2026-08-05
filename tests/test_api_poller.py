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

from automation.api.api_poller import (
    APIPoller,
)

runtime = AutomationRuntime()


def handler(event):

    print(
        event.event_type.value
    )

    print(
        event.payload
    )


runtime.event_registry.register(

    EventType.API,

    handler,

)

trigger = APITrigger(

    name="HTTPBin",

    url="https://httpbin.org/get",

    interval=5,

)

poller = APIPoller(

    trigger,

    runtime,

)

poller.start()

time.sleep(6)

poller.stop()

print("API Poller OK")
