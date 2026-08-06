from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class AutomationTemplate:
    """
    Blueprint used to generate
    an Automation object.
    """

    name: str

    trigger: str | None = None

    action: str | None = None

    target: str | None = None

    condition: str | None = None

    schedule: str | None = None

    metadata: dict[str, Any] = field(
        default_factory=dict
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

            "name": self.name,

            "trigger": self.trigger,

            "action": self.action,

            "target": self.target,

            "condition": self.condition,

            "schedule": self.schedule,

            "metadata": self.metadata,

        }

    # ---------------------------- #

    @classmethod
    def from_dict(
        cls,
        data: dict,
    ):

        return cls(

            name=data["name"],

            trigger=data.get(
                "trigger"
            ),

            action=data.get(
                "action"
            ),

            target=data.get(
                "target"
            ),

            condition=data.get(
                "condition"
            ),

            schedule=data.get(
                "schedule"
            ),

            metadata=data.get(
                "metadata",
                {},
            ),

        )

    # ---------------------------- #

    def __repr__(self):

        return (

            "<AutomationTemplate "

            f"{self.name}>"

        )
