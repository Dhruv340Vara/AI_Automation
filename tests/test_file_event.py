from automation.events import (
    FileEventFactory,
)

event = FileEventFactory.created(
    "/tmp/demo.pdf"
)

print(event)

print(event.event_type.value)

print(event.payload)

event = FileEventFactory.renamed(
    "/tmp/a.txt",
    "/tmp/b.txt",
)

print(event.payload)
