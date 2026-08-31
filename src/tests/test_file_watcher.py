import time

from automation.automation_runtime import (
    AutomationRuntime,
)

from automation.events import (
    EventType,
)

from automation.file_system import (
    FileWatcher,
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

watcher = FileWatcher(

    trigger,

    runtime,

)

watcher.start()

print(
    "Watching..."
)

try:

    while True:

        time.sleep(1)

except KeyboardInterrupt:

    watcher.stop()
