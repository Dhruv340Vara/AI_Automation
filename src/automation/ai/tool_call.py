from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4


@dataclass(slots=True)
class ToolCall:
    """
    Standard representation of an LLM tool call.
    """

    tool: str

    arguments: dict[str, Any] = field(
        default_factory=dict
    )

    call_id: str = field(
        default_factory=lambda: str(uuid4())
    )

    # -------------------------------- #

    def __post_init__(self):
        if not isinstance(self.tool, str):
            raise TypeError(
                "tool must be a string"
            )

        self.tool = self.tool.strip()

        if not self.tool:
            raise ValueError(
                "tool name cannot be empty"
            )

        if not isinstance(self.arguments, dict):
            raise TypeError(
                "arguments must be a dictionary"
            )

    # -------------------------------- #

    def to_dict(self) -> dict[str, Any]:
        return {
            "type": "tool_call",
            "id": self.call_id,
            "tool": self.tool,
            "arguments": self.arguments,
        }

    # -------------------------------- #

    @classmethod
    def from_dict(
        cls,
        data: dict[str, Any],
    ) -> "ToolCall":

        if not isinstance(data, dict):
            raise TypeError(
                "Tool call must be a dictionary"
            )

        if data.get("type") != "tool_call":
            raise ValueError(
                "Invalid tool call type"
            )

        tool = data.get("tool")

        arguments = data.get(
            "arguments",
            {},
        )

        call_id = data.get(
            "id"
        )

        obj = cls(
            tool=tool,
            arguments=arguments,
        )

        if call_id:
            obj.call_id = str(call_id)

        return obj

    # -------------------------------- #

    def is_valid(self) -> bool:
        return (
            bool(self.tool)
            and isinstance(
                self.arguments,
                dict,
            )
        )

    # -------------------------------- #

    def __repr__(self):
        return (
            f"<ToolCall "
            f"{self.tool} "
            f"id={self.call_id}>"
        )

