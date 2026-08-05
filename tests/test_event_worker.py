import time

from automation.events import (
    Event,
    EventDispatcher,
    EventListener,
    EventQueue,
    EventRegistry,
    EventType,
    EventWorker,
)

registry = EventRegistry()

queue = EventQueue()

dispatcher = EventDispatcher(
    registry
)

listener = EventListener(
    dispatcher
)

worker = EventWorker(
    queue,
    listener,
)


def handler(event):

    print(
        "Handled:",
        event.event_type.value
    )


registry.register(
    EventType.FILE_CREATED,
    handler,
)

worker.start()

queue.put(

    Event(

        event_type=EventType.FILE_CREATED,

        source="Downloads",

    )

)

time.sleep(1)

worker.stop()

print("Worker OK")
