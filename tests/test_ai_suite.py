from __future__ import annotations

print("=" * 60)
print("               AI TEST SUITE")
print("=" * 60)

from automation.ai.ai_message import (
    AIMessage,
    MessageRole,
)

from automation.ai.ai_context import (
    AIContext,
)

from automation.ai.ai_session import (
    AISession,
)

from automation.ai.ai_brain import (
    AIBrain,
)

# ==================================================
# Message
# ==================================================

print("\nTesting AIMessage...")

message = AIMessage(

    role=MessageRole.USER,

    content="Backup my Downloads every night.",

)

assert message.role == MessageRole.USER

assert message.content == (
    "Backup my Downloads every night."
)

print("PASS")

# ==================================================
# Context
# ==================================================

print("\nTesting AIContext...")

context = AIContext()

context.add_message(
    message
)

context.set_variable(
    "language",
    "Gujarati",
)

assert context.count_messages() == 1

assert (
    context.get_variable(
        "language"
    )
    == "Gujarati"
)

print("PASS")

# ==================================================
# Session
# ==================================================

print("\nTesting AISession...")

session = AISession()

session.context = context

assert session.is_active()

assert len(
    session.context
) == 1

session.close()

assert not session.is_active()

session.open()

assert session.is_active()

print("PASS")

# ==================================================
# Brain
# ==================================================

print("\nTesting AIBrain...")

brain = AIBrain()

brain.receive(
    message
)

brain.receive(

    AIMessage(

        role=MessageRole.ASSISTANT,

        content="Automation created.",

    )

)

assert len(
    brain.history()
) == 2

assert (
    brain.last_message().content
    == "Automation created."
)

brain.clear()

assert len(
    brain.history()
) == 0

print("PASS")

# ==================================================

print()

print("=" * 60)

print("ALL AI CORE TESTS PASSED")

print("=" * 60)
