from automation.ai.ai_brain import (
    AIBrain,
)

from automation.ai.ai_message import (
    AIMessage,
    MessageRole,
)

brain = AIBrain()

print(brain)

print()

brain.receive(

    AIMessage(

        role=MessageRole.USER,

        content="Hello AI",

    )

)

brain.receive(

    AIMessage(

        role=MessageRole.ASSISTANT,

        content="Hello Dhruv",

    )

)

print(brain)

print()

print(brain.last_message())

print()

print(len(brain.history()))

print()

brain.close()

print(brain.is_active())

brain.open()

print(brain.is_active())

brain.clear()

print(len(brain.history()))
