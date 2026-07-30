"""
Task Result
-----------

Stores execution result of a task.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Optional


@dataclass
class TaskResult:
    """
    Result returned after task execution.
    """

    success: bool
    message: str = ""
    data: Any = None
    error: Optional[str] = None
    completed_at: str = field(
        default_factory=lambda: datetime.now().isoformat(timespec="seconds")
    )

    def to_dict(self) -> dict:
        return {
            "success": self.success,
            "message": self.message,
            "data": self.data,
            "error": self.error,
            "completed_at": self.completed_at,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            success=data.get("success", False),
            message=data.get("message", ""),
            data=data.get("data"),
            error=data.get("error"),
            completed_at=data.get("completed_at"),
        )
