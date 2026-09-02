from __future__ import annotations
from email import message

import requests

from automation.ai.llm.llm_adapter import (
    LLMAdapter,
)

from automation.ai.llm.llm_message import (
    LLMMessage,
)

from automation.ai.llm.llm_response import (
    LLMResponse,
)


class OllamaAdapter(
    LLMAdapter,
):

    def __init__(
        self,
        model: str = "llama3",
        host: str = "http://localhost:11434",
    ):

        super().__init__(
            model=model,
        )

        self.host = host.rstrip("/")

    # ---------------------------- #

    def available(
        self,
    ) -> bool:

        try:

            response = requests.get(

                f"{self.host}/api/tags",

                timeout=3,

            )

            return (
                response.status_code
                == 200
            )

        except Exception:

            return False

    # ---------------------------- #

    def generate(self,message: LLMMessage,) -> LLMResponse:
        try:
            prompt = self._build_prompt(message)

            response = requests.post(
                f"{self.host}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                },
                timeout=120,
            )

            response.raise_for_status()

            data = response.json()

            result = LLMResponse(
                success=True,
                content=data.get("response", ""),
                model=data.get(
                    "model",
                    self.model,
                ),
                finish_reason=(
                    "stop"
                    if data.get("done")
                    else ""
                ),
            )

            result.usage = {
                "prompt_eval_count": data.get(
                    "prompt_eval_count"
                ),
                "eval_count": data.get(
                    "eval_count"
                ),
            }

            return result

        except Exception as error:
            return LLMResponse(
                success=False,
                content=str(error),
                model=self.model,
            )

    def _build_prompt(self,message: LLMMessage,) -> str:

        parts = []

        # System instruction
        if message.system:
            parts.append(message.system)

        # Relevant memories
        memories = message.context.get(
            "memories",
            [],
        )

        if memories:
            parts.append("Relevant Memories:")

            for memory in memories:
                role = memory.get("role", "")
                content = memory.get("content", "")

                if not content:
                    continue

                if role == "user":
                    parts.append(f"User: {content}")

                elif role == "assistant":
                    parts.append(f"Assistant: {content}")

        # Recent conversation
        conversation = message.context.get(
            "conversation",
            [],
        )

        if conversation:
            parts.append("Recent Conversation:")

            for item in conversation:
                role = item.get("role", "")
                content = item.get("content", "")

                if not content:
                    continue

                if role == "user":
                    parts.append(f"User: {content}")

                elif role == "assistant":
                    parts.append(f"Assistant: {content}")

        # Current user message
        parts.append(
            f"User: {message.user}"
        )

        return "\n\n".join(parts)