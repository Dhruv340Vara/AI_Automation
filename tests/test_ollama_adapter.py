from automation.ai.llm.llm_message import (
    LLMMessage,
)

from automation.ai.llm.ollama_adapter import (
    OllamaAdapter,
)

llm = OllamaAdapter()

print(llm)

print()

print(

    llm.available()

)

print()

if llm.available():

    response = llm.generate(

        LLMMessage(

            system="You are an AI assistant.",

            user="Say Hello",

        )

    )

    print(response)

    print()

    print(response.content)

else:

    print(

        "Ollama server not running."

    )
