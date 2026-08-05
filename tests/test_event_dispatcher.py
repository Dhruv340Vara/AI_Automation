from automation.events import (
    Event,
    EventDispatcher,
    EventRegistry,
    EventType,
)


registry = EventRegistry()


def print_event(event):

    print(
        "Received:",
        event.event_type,
        event.source,
    )


registry.register(
    EventType.FILE_CREATED,
    print_event,
)

dispatcher = EventDispatcher(
    registry
)

event = Event(
    event_type=EventType.FILE_CREATED,
    source="Downloads",
)

count = dispatcher.dispatch(
    event
)

print("Handlers:", count)

print("Status:", event.status.value)
