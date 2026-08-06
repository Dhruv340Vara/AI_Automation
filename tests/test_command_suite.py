"""
Command Layer Test Suite
"""

from automation.assistant.command import (
    Command,
    CommandStatus,
)

from automation.assistant.command_registry import (
    CommandRegistry,
)

from automation.assistant.command_matcher import (
    CommandMatcher,
)

from automation.assistant.command_router import (
    CommandRouter,
)

from automation.assistant.command_executor import (
    CommandExecutor,
)


# ------------------------------------- #

def call_handler(command):

    print(

        f"Calling {command.get_parameter('contact')}"

    )


def torch_handler(command):

    print(

        f"Torch {command.get_parameter('state')}"

    )


# ------------------------------------- #

print("=" * 60)
print("          COMMAND TEST SUITE")
print("=" * 60)
print()

# ------------------------------------- #
print("Creating Components...")

matcher = CommandMatcher()

registry = CommandRegistry()

router = CommandRouter(
    matcher,
    registry,
)

executor = CommandExecutor()

print("PASS")
print()

# ------------------------------------- #
print("Registering Commands...")

matcher.register(
    "call",
    "call",
    "dial",
    "phone",
)

matcher.register(
    "torch",
    "torch",
    "flashlight",
)

registry.register(
    "call",
    call_handler,
)

registry.register(
    "torch",
    torch_handler,
)

assert registry.count() == 2

print("PASS")
print()

# ------------------------------------- #
print("Testing Call Command...")

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

assert handler is not None

assert executor.execute(

    command,

    handler,

)

assert (

    command.status

    == CommandStatus.COMPLETED

)

print("PASS")
print()

# ------------------------------------- #
print("Testing Torch Command...")

command = Command(

    name="voice",

    description="Turn on flashlight",

)

command.set_parameter(

    "state",

    "ON",

)

handler = router.route(
    command
)

assert handler is not None

assert executor.execute(

    command,

    handler,

)

print("PASS")
print()

# ------------------------------------- #
print("Testing Unknown Command...")

command = Command(

    name="voice",

    description="Open Chrome",

)

handler = router.route(
    command
)

assert handler is None

assert not executor.execute(

    command,

    handler,

)

assert (

    command.status

    == CommandStatus.FAILED

)

print("PASS")
print()

# ------------------------------------- #
print("Executed Commands:")

print(

    executor.count()

)

print()

print("=" * 60)
print("ALL COMMAND TESTS PASSED")
print("=" * 60)
