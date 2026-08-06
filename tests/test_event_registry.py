from automation.events import (
    EventRegistry,
    EventType,
)

registry = EventRegistry()


def on_file(event):
    print(event)


registry.register(
    EventType.FILE_CREATED,
    on_file,
)

print(
    registry.has_handlers(
        EventType.FILE_CREATED
    )
)

print(
    registry.get_handlers(
        EventType.FILE_CREATED
    )
)
