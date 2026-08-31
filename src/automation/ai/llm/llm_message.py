from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class LLMMessage:
    """
    Request sent to an LLM.
    """

    system: str = ""

    user: str = ""

    context: dict[str, Any] = field(
        default_factory=dict
    )

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    created_at: str = field(
        default_factory=lambda:
        datetime.now().isoformat(
            timespec="seconds"
        )
    )

    # ---------------------------- #

    def set_context(
        self,
        key: str,
        value: Any,
    ):

        self.context[key] = value

    # ---------------------------- #

    def get_context(
        self,
        key: str,
        default=None,
    ):

        return self.context.get(
            key,
            default,
        )

    # ---------------------------- #

    def set_metadata(
        self,
        key: str,
        value: Any,
    ):

        self.metadata[key] = value

    # ---------------------------- #

    def get_metadata(
        self,
        key: str,
        default=None,
    ):

        return self.metadata.get(
            key,
            default,
        )

    # ---------------------------- #

    def to_dict(
        self,
    ):

        return {

            "system":
                self.system,

            "user":
                self.user,

            "context":
                self.context,

            "metadata":
                self.metadata,

            "created_at":
                self.created_at,

        }

    # ---------------------------- #

    @classmethod
    def from_dict(
        cls,
        data: dict,
    ):

        obj = cls(

            system=data.get(
                "system",
                "",
            ),

            user=data.get(
                "user",
                "",
            ),

            context=data.get(
                "context",
                {},
            ),

            metadata=data.get(
                "metadata",
                {},
            ),

        )

        obj.created_at = data.get(
            "created_at",
            obj.created_at,
        )

        return obj

    # ---------------------------- #

    def __repr__(
        self,
    ):

        return (
            "<LLMMessage "
            f"user='{self.user[:30]}'>"
        )
