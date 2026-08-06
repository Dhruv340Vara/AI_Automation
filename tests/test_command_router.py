from automation.assistant.command import Command
from automation.assistant.command_matcher import CommandMatcher
from automation.assistant.command_registry import CommandRegistry
from automation.assistant.command_router import CommandRouter


def call_handler(command):

    print("Calling:", command.get_parameter("contact"))


def torch_handler(command):

    print("Torch:", command.get_parameter("state"))


matcher = CommandMatcher()

matcher.register(
    "call",
    "call",
    "dial",
)

matcher.register(
    "torch",
    "torch",
    "flashlight",
)


registry = CommandRegistry()

registry.register(
    "call",
    call_handler,
)

registry.register(
    "torch",
    torch_handler,
)


router = CommandRouter(
    matcher,
    registry,
)

print(router)

print()

command = Command(
    name="voice",
    description="Call Mummy",
)

command.set_parameter(
    "contact",
    "Mummy",
)

handler = router.route(
    command
)

print(handler)

print()

if handler:

    handler(command)

print()

unknown = Command(
    name="voice",
    description="Open Chrome",
)

print(
    router.route(
        unknown
    )
)

print()

print(
    router.can_route(
        command
    )
)

print(
    router.can_route(
        unknown
    )
)
