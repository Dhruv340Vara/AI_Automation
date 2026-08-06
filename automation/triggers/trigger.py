from __future__ import annotations

import uuid

from datetime import datetime

from automation.triggers.trigger_types import (
    TriggerType,
)


class Trigger:

    def __init__(

        self,

        trigger_type: TriggerType,

        name: str,

        metadata=None,

        enabled=True,

    ):

        self.trigger_id = str(uuid.uuid4())

        self.trigger_type = trigger_type

        self.name = name

        self.metadata = metadata or {}

        self.enabled = enabled

        self.created_at = datetime.now()

        self.updated_at = self.created_at

    def enable(self):

        self.enabled = True

        self.touch()

    def disable(self):

        self.enabled = False

        self.touch()

    def touch(self):

        self.updated_at = datetime.now()

    def to_dict(self):

        return {

            "trigger_id": self.trigger_id,

            "trigger_type": self.trigger_type.value,

            "name": self.name,

            "metadata": self.metadata,

            "enabled": self.enabled,

            "created_at": self.created_at.isoformat(),

            "updated_at": self.updated_at.isoformat(),

        }

    @classmethod
    def from_dict(cls, data):

        obj = cls(

            trigger_type=TriggerType(
                data["trigger_type"]
            ),

            name=data["name"],

            metadata=data.get(
                "metadata",
                {},
            ),

            enabled=data.get(
                "enabled",
                True,
            ),

        )

        obj.trigger_id = data["trigger_id"]

        obj.created_at = datetime.fromisoformat(
            data["created_at"]
        )

        obj.updated_at = datetime.fromisoformat(
            data["updated_at"]
        )

        return obj

    def __repr__(self):

        state = (
            "enabled"
            if self.enabled
            else "disabled"
        )

        return (
            f"<Trigger("
            f"{self.name}, "
            f"{self.trigger_type.value}, "
            f"{state})>"
        )
