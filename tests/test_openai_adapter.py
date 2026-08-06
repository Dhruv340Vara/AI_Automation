import os

from automation.ai.llm.llm_message import (
    LLMMessage,
)

from automation.ai.llm.openai_adapter import (
    OpenAIAdapter,
)

api_key = os.getenv(
    "OPENAI_API_KEY"
)

if not api_key:

    print(
        "OPENAI_API_KEY not found."
    )

    raise SystemExit

llm = OpenAIAdapter(
    api_key=api_key,
)

print(llm)

print()

print(
    llm.available()
)

print()

response = llm.generate(

    LLMMessage(

        system="You are an AI assistant.",

        user="Say Hello",

    )

)

print(response)

print()

print(response.content)

print()

print(response.usage)
