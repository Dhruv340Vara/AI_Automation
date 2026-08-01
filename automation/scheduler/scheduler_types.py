"""
scheduler_types.py

Shared scheduler enums.
"""

from enum import Enum


class ExecutionResult(Enum):
    """
    Result returned by a task handler.
    """

    SUCCESS = "success"

    FAILED = "failed"

    RETRY = "retry"

    CANCEL = "cancel"


class RetryPolicy(Enum):
    """
    Retry policy.
    """

    NEVER = "never"

    IMMEDIATE = "immediate"

    DELAY = "delay"


class SchedulePriority(Enum):
    """
    Scheduler priority.
    """

    LOW = "low"

    NORMAL = "normal"

    HIGH = "high"
