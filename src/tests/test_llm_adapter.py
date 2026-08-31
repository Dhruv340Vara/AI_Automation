from automation.ai.llm.llm_adapter import (
    LLMAdapter,
)

from automation.ai.llm.llm_message import (
    LLMMessage,
)

from automation.ai.llm.llm_response import (
    LLMResponse,
)


class DemoLLM(
    LLMAdapter,
):

    def __init__(
        self,
    ):

        super().__init__(
            model="demo",
        )

    def available(
        self,
    ):

        return True

    def generate(
        self,
        message: LLMMessage,
    ):

        return LLMResponse(

            success=True,

            content=f"Echo: {message.user}",

            model=self.model,

            finish_reason="stop",

        )


llm = DemoLLM()

print(llm)

print()

print(

    llm.available()

)

print()

response = llm.generate(

    LLMMessage(

        user="Hello AI",

    )

)

print(response)

print()

print(response.content)

print()

print(response.model)
