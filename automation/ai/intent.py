from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from automation.ai.intent_types import (
    IntentType,
)


@dataclass(slots=True)
class Intent:
    """
    Represents a parsed user intent.
    """

    intent_type: IntentType

    confidence: float = 1.0

    parameters: dict[str, Any] = field(
        default_factory=dict
    )

    source: str = "rule"

    # -------------------------------- #

    def set_parameter(
        self,
        key: str,
        value: Any,
    ):

        self.parameters[key] = value

    # -------------------------------- #

    def get_parameter(
        self,
        key: str,
        default=None,
    ):

        return self.parameters.get(
            key,
            default,
        )

    # -------------------------------- #

    def has_parameter(
        self,
        key: str,
    ):

        return key in self.parameters

    # -------------------------------- #

    def remove_parameter(
        self,
        key: str,
    ):

        return self.parameters.pop(
            key,
            None,
        )

    # -------------------------------- #

    def clear_parameters(
        self,
    ):

        self.parameters.clear()

    # -------------------------------- #

    def to_dict(
        self,
    ):

        return {

            "intent_type":
                self.intent_type.value,

            "confidence":
                self.confidence,

            "parameters":
                self.parameters,

            "source":
                self.source,

        }

    # -------------------------------- #

    @classmethod
    def from_dict(
        cls,
        data: dict,
    ):

        return cls(

            intent_type=IntentType(
                data["intent_type"]
            ),

            confidence=data.get(
                "confidence",
                1.0,
            ),

            parameters=data.get(
                "parameters",
                {},
            ),

            source=data.get(
                "source",
                "rule",
            ),

        )

    # -------------------------------- #

    def __repr__(
        self,
    ):

        return (

            "<Intent "

            f"{self.intent_type.value} "

            f"confidence={self.confidence:.2f}>"

        )
