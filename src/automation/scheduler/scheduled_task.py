from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any
from uuid import uuid4

class ScheduleStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    PAUSED = "paused"
    COMPLETED = "completed"
    FAILED = "failed"      # NEW
    CANCELLED = "cancelled"

class ScheduleType(Enum):
    ONCE = "once"
    INTERVAL = "interval"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"

@dataclass
class ScheduledTask:
    automation_id: str
    schedule_type: ScheduleType
    next_run: datetime
    interval: int | None = None
    weekday: int | None = None
    day: int | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
    task_id: str = field(
        default_factory=lambda: str(uuid4())
    )
    status: ScheduleStatus = ScheduleStatus.PENDING
    last_run: datetime | None = None
    created_at: datetime = field(
        default_factory=datetime.now
    )

    def should_run(self):
        if self.status != ScheduleStatus.PENDING:
            return False
        return datetime.now() >= self.next_run

    def mark_running(self):
        self.status = ScheduleStatus.RUNNING

    def mark_failed(self):
        self.status = ScheduleStatus.FAILED
        self.last_run = datetime.now()

    def mark_completed(self):
        self.status = ScheduleStatus.COMPLETED
        self.last_run = datetime.now()

    def pause(self):
        self.status = ScheduleStatus.PAUSED

    def resume(self):
        self.status = ScheduleStatus.PENDING

    def cancel(self):
        self.status = ScheduleStatus.CANCELLED

    def to_dict(self):
        return {
            "task_id": self.task_id,
            "automation_id": self.automation_id,
            "schedule_type": self.schedule_type.value,
            "status": self.status.value,
            "next_run": self.next_run.isoformat(),
            "last_run": (
                self.last_run.isoformat()
                if self.last_run
                else None
            ),
            "interval": self.interval,
            "weekday": self.weekday,
            "day": self.day,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
        }

    @classmethod
    def from_dict(cls, data):
        obj = cls(
            automation_id=data["automation_id"],
            schedule_type=ScheduleType(
                data["schedule_type"]
            ),
            next_run=datetime.fromisoformat(
                data["next_run"]
            ),
            interval=data.get("interval"),
            weekday=data.get("weekday"),
            day=data.get("day"),
            metadata=data.get("metadata", {})
        )
        obj.task_id = data["task_id"]
        obj.status = ScheduleStatus(
            data["status"]
        )
        if data["last_run"]:
            obj.last_run = datetime.fromisoformat(
                data["last_run"]
            )
        obj.created_at = datetime.fromisoformat(
            data["created_at"]
        )
        return obj

    def __repr__(self):
        return (
            f"<ScheduledTask("
            f"{self.task_id}, "
            f"{self.schedule_type.value}, "
            f"{self.status.value}"
            f")>"
        )
