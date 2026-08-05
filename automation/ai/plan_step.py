from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class StepStatus(Enum):

    PENDING = "pending"

    RUNNING = "running"

    COMPLETED = "completed"

    FAILED = "failed"


@dataclass(slots=True)
class PlanStep:
    """
    Represents one execution step
    inside an execution plan.
    """

    name: str

    description: str = ""

    parameters: dict[str, Any] = field(
        default_factory=dict
    )

    status: StepStatus = (
        StepStatus.PENDING
    )

    # -------------------------------- #

    def start(self):

        self.status = (
            StepStatus.RUNNING
        )

    # -------------------------------- #

    def complete(self):

        self.status = (
            StepStatus.COMPLETED
        )

    # -------------------------------- #

    def fail(self):

        self.status = (
            StepStatus.FAILED
        )

    # -------------------------------- #

    def reset(self):

        self.status = (
            StepStatus.PENDING
        )

    # -------------------------------- #

    def is_pending(self):

        return (
            self.status
            == StepStatus.PENDING
        )

    # -------------------------------- #

    def is_running(self):

        return (
            self.status
            == StepStatus.RUNNING
        )

    # -------------------------------- #

    def is_completed(self):

        return (
            self.status
            == StepStatus.COMPLETED
        )

    # -------------------------------- #

    def is_failed(self):

        return (
            self.status
            == StepStatus.FAILED
        )

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

    def to_dict(self):

        return {

            "name": self.name,

            "description": self.description,

            "parameters": self.parameters,

            "status": self.status.value,

        }

    # -------------------------------- #

    @classmethod
    def from_dict(
        cls,
        data: dict,
    ):

        return cls(

            name=data["name"],

            description=data.get(
                "description",
                "",
            ),

            parameters=data.get(
                "parameters",
                {},
            ),

            status=StepStatus(
                data.get(
                    "status",
                    "pending",
                )
            ),

        )

    # -------------------------------- #

    def __repr__(self):

        return (

            "<PlanStep "

            f"{self.name} "

            f"({self.status.value})>"

        )
