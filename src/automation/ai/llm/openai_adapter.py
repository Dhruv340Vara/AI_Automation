from __future__ import annotations

from openai import OpenAI

from automation.ai.llm.llm_adapter import (
    LLMAdapter,
)

from automation.ai.llm.llm_message import (
    LLMMessage,
)

from automation.ai.llm.llm_response import (
    LLMResponse,
)


class OpenAIAdapter(LLMAdapter):
    """
    OpenAI LLM Adapter.
    """

    def __init__(
        self,
        api_key: str,
        model: str = "gpt-5.5",
    ):

        super().__init__(model)

        self.client = OpenAI(
            api_key=api_key,
        )

    # ---------------------------- #

    def available(self) -> bool:

        try:

            self.client.models.list()

            return True

        except Exception:

            return False

    # ---------------------------- #

    def generate(
        self,
        message: LLMMessage,
    ) -> LLMResponse:

        try:

            response = self.client.chat.completions.create(

                model=self.model,

                messages=[

                    {
                        "role": "system",
                        "content": message.system,
                    },

                    {
                        "role": "user",
                        "content": message.user,
                    },

                ],

            )

            answer = response.choices[0]

            result = LLMResponse(

                success=True,

                content=answer.message.content,

                model=response.model,

                finish_reason=(
                    answer.finish_reason
                    or ""
                ),

            )

            result.usage = {

                "prompt_tokens":
                    response.usage.prompt_tokens,

                "completion_tokens":
                    response.usage.completion_tokens,

                "total_tokens":
                    response.usage.total_tokens,

            }

            result.metadata = {

                "provider": "openai",

            }

            return result

        except Exception as error:

            return LLMResponse(

                success=False,

                content=str(error),

                model=self.model,

            )
