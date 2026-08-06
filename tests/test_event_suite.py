from automation.events import (
    Event,
    EventDispatcher,
    EventListener,
    EventQueue,
    EventRegistry,
    EventStatus,
    EventType,
)

print("=" * 60)
print("            EVENT TEST SUITE")
print("=" * 60)

registry = EventRegistry()

handled_events = []


def file_handler(event):

    handled_events.append(event.event_type)

    print(
        "[Handler]",
        event.event_type.value,
        event.source,
    )


registry.register(
    EventType.FILE_CREATED,
    file_handler,
)

dispatcher = EventDispatcher(
    registry
)

listener = EventListener(
    dispatcher
)

queue = EventQueue()

event = Event(
    event_type=EventType.FILE_CREATED,
    source="Downloads",
)

print("\nCreating Event...")

queue.put(event)

assert queue.size() == 1

queued_event = queue.get()

assert queued_event is event

count = listener.listen(
    queued_event
)

queue.task_done()

assert count == 1

assert listener.received_count == 1

assert event.status == EventStatus.COMPLETED

assert handled_events == [
    EventType.FILE_CREATED
]

assert queue.empty()

print("\nAll Assertions Passed")

print("\nEvent Status :", event.status.value)

print("Handlers     :", count)

print("Received     :", listener.received_count)

print("Queue Empty  :", queue.empty())

print("\n" + "=" * 60)

print("EVENT SUITE PASSED")

print("=" * 60)
