import time

from automation.automation_runtime import (
    AutomationRuntime,
)

from automation.events import (
    EventType,
)

from automation.triggers import (
    FileTrigger,
)

runtime = AutomationRuntime()

def handler(event):

    print(
        event.event_type.value,
        event.payload,
    )

runtime.event_registry.register(

    EventType.FILE_CREATED,

    handler,

)

trigger = FileTrigger(

    name="Downloads",

    path="test_folder",

    events=["created"],

)

runtime.register_file_trigger(
    trigger
)

runtime.start()

print(
    "Runtime Started"
)

try:

    while True:

        time.sleep(1)

except KeyboardInterrupt:

    runtime.stop()

    print("Stopped")
