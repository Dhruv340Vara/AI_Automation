from __future__ import annotations
from automation.events.event_types import EventType
from copy import deepcopy
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any
from uuid import uuid4


class EventPriority(Enum):
    LOW = "low"
    NORMAL = "normal"
    HIGH = "high"
    CRITICAL = "critical"


class EventStatus(Enum):
    CREATED = "created"
    QUEUED = "queued"
    DISPATCHED = "dispatched"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


@dataclass
class Event:

    event_type: EventType

    source: str

    payload: dict[str, Any] = field(default_factory=dict)

    metadata: dict[str, Any] = field(default_factory=dict)

    priority: EventPriority = EventPriority.NORMAL

    event_id: str = field(
        default_factory=lambda: str(uuid4())
    )

    status: EventStatus = EventStatus.CREATED

    created_at: datetime = field(
        default_factory=datetime.now
    )

    updated_at: datetime = field(
        default_factory=datetime.now
    )

    # ------------------------------------------------ #

    def validate(self) -> bool:

        if not isinstance(
            self.event_type,
            EventType,
        ):
            raise TypeError(
                "event_type must be EventType."
            )

        if not self.source.strip():
            raise ValueError(
                "Event source cannot be empty."
            )

        if not isinstance(self.payload, dict):
            raise TypeError(
                "payload must be a dictionary."
            )

        if not isinstance(self.metadata, dict):
            raise TypeError(
                "metadata must be a dictionary."
            )

        return True

    # ------------------------------------------------ #

    def touch(self):

        self.updated_at = datetime.now()

    # ------------------------------------------------ #

    def queue(self):

        self.status = EventStatus.QUEUED
        self.touch()

    def dispatch(self):

        self.status = EventStatus.DISPATCHED
        self.touch()

    def processing(self):

        self.status = EventStatus.PROCESSING
        self.touch()

    def complete(self):

        self.status = EventStatus.COMPLETED
        self.touch()

    def fail(self):

        self.status = EventStatus.FAILED
        self.touch()

    def cancel(self):

        self.status = EventStatus.CANCELLED
        self.touch()

    # ------------------------------------------------ #

    def copy(self):

        clone = deepcopy(self)

        clone.event_id = str(uuid4())

        clone.created_at = datetime.now()

        clone.updated_at = clone.created_at

        clone.status = EventStatus.CREATED

        return clone

    # ------------------------------------------------ #

    def to_dict(self):

        return {
            "event_id": self.event_id,
            "event_type": self.event_type.value,
            "source": self.source,
            "payload": self.payload,
            "metadata": self.metadata,
            "priority": self.priority.value,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @classmethod
    def from_dict(
        cls,
        data: dict[str, Any],
    ):

        event = cls(
            event_type=EventType.from_string(
                data["event_type"]
            ),
            source=data["source"],
            payload=data.get(
                "payload",
                {},
            ),
            metadata=data.get(
                "metadata",
                {},
            ),
            priority=EventPriority(
                data.get(
                    "priority",
                    EventPriority.NORMAL.value,
                )
            ),
        )

        event.event_id = data["event_id"]

        event.status = EventStatus(
            data.get(
                "status",
                EventStatus.CREATED.value,
            )
        )

        event.created_at = datetime.fromisoformat(
            data["created_at"]
        )

        event.updated_at = datetime.fromisoformat(
            data["updated_at"]
        )

        return event

    # ------------------------------------------------ #

    def __repr__(self):

        return (
            f"<Event("
            f"{self.event_type}, "
            f"{self.status.value}, "
            f"{self.priority.value}"
            f")>"
        )
