from automation.ai.llm.llm_message import (
    LLMMessage,
)

message = LLMMessage(

    system="You are an AI assistant.",

    user="Backup my Downloads every night.",

)

print(message)

print()

message.set_context(

    "language",

    "Gujarati",

)

message.set_metadata(

    "model",

    "llama3",

)

print(

    message.get_context(

        "language"

    )

)

print()

print(

    message.get_metadata(

        "model"

    )

)

print()

print(

    message.to_dict()

)

print()

copy = LLMMessage.from_dict(

    message.to_dict()

)

print(copy)
