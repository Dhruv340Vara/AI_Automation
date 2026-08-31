from automation.events import (
    Event,
    EventQueue,
    EventStatus,
    EventType,
)

queue = EventQueue()

event = Event(
    event_type=EventType.FILE_CREATED,
    source="Downloads",
)

queue.put(event)

print(
    "Queue Size:",
    queue.size(),
)

queued = queue.get()

print(
    "Same Event:",
    queued is event,
)

print(
    "Status:",
    queued.status.value,
)

queue.task_done()

print(
    "Queue Empty:",
    queue.empty(),
)
