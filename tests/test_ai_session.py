from automation.ai.ai_session import (
    AISession,
)

from automation.ai.ai_message import (
    AIMessage,
    MessageRole,
)

session = AISession()

session.context.add_message(

    AIMessage(

        role=MessageRole.USER,

        content="Hello",

    )

)

session.touch()

print(session)

print()

print(session.is_active())

print()

print(session.to_dict())

print()

copy = AISession.from_dict(
    session.to_dict()
)

print(copy)

print(copy.context.last_message())

print()

session.close()

print(session.is_active())

session.open()

print(session.is_active())

session.reset()

print(len(session.context))
