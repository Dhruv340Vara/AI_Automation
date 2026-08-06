from automation.ai.llm.llm_response import (
    LLMResponse,
)

response = LLMResponse(

    success=True,

    content="Automation created successfully.",

    model="llama3",

    finish_reason="stop",

)

print(response)

print()

response.set_usage(

    "prompt_tokens",

    120,

)

response.set_usage(

    "completion_tokens",

    35,

)

response.set_metadata(

    "provider",

    "ollama",

)

print(

    response.is_success()

)

print()

print(

    response.get_usage(

        "prompt_tokens"

    )

)

print()

print(

    response.get_metadata(

        "provider"

    )

)

print()

print(

    response.to_dict()

)

print()

copy = LLMResponse.from_dict(

    response.to_dict()

)

print(copy)
