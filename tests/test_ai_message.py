from automation.ai.ai_message import (

    AIMessage,

    MessageRole,

)

message = AIMessage(

    role=MessageRole.USER,

    content="Backup my Downloads every night.",

)

print(message)

print()

print(message.to_dict())

print()

copy = AIMessage.from_dict(

    message.to_dict()

)

print(copy)

print(copy.role)

print(copy.content)

print(copy.metadata)
