from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class LLMResponse:
    """
    Standard response returned by any LLM.
    """

    success: bool = True

    content: str = ""

    model: str = ""

    finish_reason: str = ""

    usage: dict[str, Any] = field(
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

    def is_success(self):

        return self.success

    # ---------------------------- #

    def set_usage(
        self,
        key: str,
        value: Any,
    ):

        self.usage[key] = value

    # ---------------------------- #

    def get_usage(
        self,
        key: str,
        default=None,
    ):

        return self.usage.get(
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

    def to_dict(self):

        return {

            "success":
                self.success,

            "content":
                self.content,

            "model":
                self.model,

            "finish_reason":
                self.finish_reason,

            "usage":
                self.usage,

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

            success=data.get(
                "success",
                True,
            ),

            content=data.get(
                "content",
                "",
            ),

            model=data.get(
                "model",
                "",
            ),

            finish_reason=data.get(
                "finish_reason",
                "",
            ),

            usage=data.get(
                "usage",
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

    def __repr__(self):

        status = (
            "success"
            if self.success
            else "failed"
        )

        return (
            f"<LLMResponse "
            f"{status} "
            f"model='{self.model}'>"
        )
