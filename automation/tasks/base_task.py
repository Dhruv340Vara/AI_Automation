"""
Base Task
---------

Base class for all automation tasks.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from uuid import uuid4

from automation.tasks.task_result import TaskResult


class TaskStatus(Enum):
    """
    Possible task states.
    """

    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"


class BaseTask(ABC):
    """
    Base class for every automation task.
    """

    def __init__(self, name: str, description: str = ""):

        self.task_id = str(uuid4())

        self.name = name
        self.description = description

        self.status = TaskStatus.PENDING

        self.created_at = datetime.now()
        self.started_at = None
        self.finished_at = None

    @abstractmethod
    def run(self) -> TaskResult:
        """
        Task logic.

        Must return TaskResult.
        """
        raise NotImplementedError

    def execute(self) -> TaskResult:
        """
        Executes task safely.
        """

        self.status = TaskStatus.RUNNING
        self.started_at = datetime.now()

        try:

            result = self.run()

            if result.success:
                self.status = TaskStatus.SUCCESS
            else:
                self.status = TaskStatus.FAILED

        except Exception as exc:

            result = TaskResult(
                success=False,
                message="Task execution failed.",
                error=str(exc),
            )

            self.status = TaskStatus.FAILED

        self.finished_at = datetime.now()

        return result

    def execution_time(self):
        """
        Returns execution duration in seconds.
        """

        if self.started_at and self.finished_at:
            return (self.finished_at - self.started_at).total_seconds()

        return None

    def to_dict(self):

        return {
            "task_id": self.task_id,
            "name": self.name,
            "description": self.description,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(timespec="seconds"),
            "started_at": (
                self.started_at.isoformat(timespec="seconds")
                if self.started_at
                else None
            ),
            "finished_at": (
                self.finished_at.isoformat(timespec="seconds")
                if self.finished_at
                else None
            ),
        }

    def __repr__(self):

        return (
            f"<{self.__class__.__name__}"
            f"(id={self.task_id}, status={self.status.value})>"
        )
