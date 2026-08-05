from automation.events import (
    Event,
    EventDispatcher,
    EventListener,
    EventRegistry,
    EventType,
)


registry = EventRegistry()


def on_file(event):

    print(
        "Handled:",
        event.event_type.value,
    )


registry.register(
    EventType.FILE_CREATED,
    on_file,
)

dispatcher = EventDispatcher(
    registry
)

listener = EventListener(
    dispatcher
)

event = Event(
    event_type=EventType.FILE_CREATED,
    source="Downloads",
)

count = listener.listen(
    event
)

print(
    "Executed:",
    count,
)

print(
    "Received:",
    listener.received_count,
)

print(
    "Status:",
    event.status.value,
)
