from __future__ import annotations

import json
from typing import Any

from automation.ai.tool_call import ToolCall


class ToolCallParser:
    """
    Parses structured LLM responses.

    Supported response types:
    - tool_call
    - final_answer
    """

    @staticmethod
    def parse(content: str) -> dict[str, Any]:
        if not isinstance(content, str):
            raise TypeError("LLM response must be a string")

        text = content.strip()

        if not text:
            raise ValueError("LLM response cannot be empty")

        try:
            data = json.loads(text)
        except json.JSONDecodeError as exc:
            raise ValueError(
                "LLM response is not valid JSON"
            ) from exc

        if not isinstance(data, dict):
            raise ValueError(
                "LLM response must be a JSON object"
            )

        response_type = data.get("type")

        if response_type == "tool_call":
            tool_call = ToolCall.from_dict(data)

            return {
                "type": "tool_call",
                "tool_call": tool_call,
            }

        if response_type == "final_answer":
            content = data.get("content")

            if not isinstance(content, str):
                raise ValueError(
                    "final_answer content must be a string"
                )

            return {
                "type": "final_answer",
                "content": content,
            }

        raise ValueError(
            f"Unsupported LLM response type: {response_type}"
        )
