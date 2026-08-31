from automation.assistant.command_registry import (
    CommandRegistry,
)


def call_handler():

    print("Calling...")


def torch_handler():

    print("Torch...")


registry = CommandRegistry()

print(registry)

print()

registry.register(
    "call",
    call_handler,
)

registry.register(
    "torch",
    torch_handler,
)

print(
    registry.count()
)

print()

print(
    registry.names()
)

print()

print(
    registry.exists(
        "call"
    )
)

print()

handler = registry.get(
    "call"
)

handler()

print()

registry.unregister(
    "call"
)

print(
    registry.names()
)

print()

registry.clear()

print(
    registry.count()
)
