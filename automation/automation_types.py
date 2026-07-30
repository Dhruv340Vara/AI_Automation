"""
automation_types.py

Core Automation data model.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any
from uuid import uuid4


class AutomationStatus(Enum):
    """
    Automation state.
    """

    ENABLED = "enabled"
    DISABLED = "disabled"


@dataclass
class Automation:
    """
    Represents one automation.

    Example:
        Every day 9 AM
            ↓
        Run Backup
    """

    name: str

    description: str = ""

    trigger: dict[str, Any] = field(default_factory=dict)

    action: dict[str, Any] = field(default_factory=dict)

    metadata: dict[str, Any] = field(default_factory=dict)

    automation_id: str = field(default_factory=lambda: str(uuid4()))

    status: AutomationStatus = AutomationStatus.ENABLED

    created_at: str = field(
        default_factory=lambda: datetime.now().isoformat(timespec="seconds")
    )

    updated_at: str = field(
        default_factory=lambda: datetime.now().isoformat(timespec="seconds")
    )

    def enable(self):

        self.status = AutomationStatus.ENABLED
        self.touch()

    def disable(self):

        self.status = AutomationStatus.DISABLED
        self.touch()

    def is_enabled(self):

        return self.status == AutomationStatus.ENABLED

    def touch(self):

        self.updated_at = datetime.now().isoformat(timespec="seconds")

    def validate(self):
        """
        Basic validation.
        """

        if not self.name.strip():
            raise ValueError("Automation name cannot be empty.")

        if not isinstance(self.trigger, dict):
            raise TypeError("trigger must be a dictionary.")

        if not isinstance(self.action, dict):
            raise TypeError("action must be a dictionary.")

        if not isinstance(self.metadata, dict):
            raise TypeError("metadata must be a dictionary.")

        return True

    def to_dict(self):

        return {
            "automation_id": self.automation_id,
            "name": self.name,
            "description": self.description,
            "status": self.status.value,
            "trigger": self.trigger,
            "action": self.action,
            "metadata": self.metadata,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    @classmethod
    def from_dict(cls, data: dict):

        obj = cls(
            name=data["name"],
            description=data.get("description", ""),
            trigger=data.get("trigger", {}),
            action=data.get("action", {}),
            metadata=data.get("metadata", {}),
        )

        obj.automation_id = data.get(
            "automation_id",
            str(uuid4())
        )

        obj.status = AutomationStatus(
            data.get(
                "status",
                "enabled"
            )
        )

        obj.created_at = data.get(
            "created_at",
            obj.created_at
        )

        obj.updated_at = data.get(
            "updated_at",
            obj.updated_at
        )

        return obj

    def __repr__(self):

        return (
            f"<Automation("
            f"{self.name}, "
            f"{self.status.value}"
            f")>"
        )
