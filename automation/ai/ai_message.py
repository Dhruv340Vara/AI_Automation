from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any
import uuid


class MessageRole(Enum):

    SYSTEM = "system"

    USER = "user"

    ASSISTANT = "assistant"

    TOOL = "tool"


@dataclass(slots=True)
class AIMessage:

    role: MessageRole

    content: str

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    message_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    created_at: datetime = field(
        default_factory=datetime.utcnow
    )

    def to_dict(self):

        return {

            "id": self.message_id,

            "role": self.role.value,

            "content": self.content,

            "metadata": self.metadata,

            "created_at": (
                self.created_at.isoformat()
            ),
        }

    @classmethod
    def from_dict(
        cls,
        data: dict,
    ):

        return cls(

            role=MessageRole(
                data["role"]
            ),

            content=data["content"],

            metadata=data.get(
                "metadata",
                {},
            ),

            message_id=data.get(
                "id",
                str(uuid.uuid4()),
            ),

            created_at=datetime.fromisoformat(
                data["created_at"]
            )
            if "created_at" in data
            else datetime.utcnow(),

        )

    def __repr__(self):

        preview = self.content

        if len(preview) > 40:

            preview = preview[:37] + "..."

        return (

            "<AIMessage "

            f"{self.role.value} "

            f"'{preview}'>"

        )
