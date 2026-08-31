from automation.ai.ai_context import (
    AIContext,
)

from automation.ai.ai_message import (
    AIMessage,
    MessageRole,
)

context = AIContext()

context.add_message(

    AIMessage(

        role=MessageRole.USER,

        content="Hello AI",

    )

)

context.add_message(

    AIMessage(

        role=MessageRole.ASSISTANT,

        content="Hello Dhruv",

    )

)

context.set_variable(

    "language",

    "Gujarati",

)

print(context)

print()

print(context.last_message())

print()

print(context.get_variable("language"))

print()

print(context.to_dict())

print()

copy = AIContext.from_dict(
    context.to_dict()
)

print(copy)

print(copy.count_messages())
