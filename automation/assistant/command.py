"""
command.py

Base class for every assistant command.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any
from uuid import uuid4


class CommandStatus(Enum):

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class Command:

    name: str

    description: str = ""

    parameters: dict[str, Any] = field(
        default_factory=dict
    )

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    command_id: str = field(
        default_factory=lambda: str(uuid4())
    )

    status: CommandStatus = CommandStatus.PENDING

    created_at: str = field(
        default_factory=lambda:
        datetime.now().isoformat(
            timespec="seconds"
        )
    )

    # ---------------------------- #

    def set_parameter(
        self,
        key: str,
        value: Any,
    ):

        self.parameters[key] = value

    # ---------------------------- #

    def get_parameter(
        self,
        key: str,
        default=None,
    ):

        return self.parameters.get(
            key,
            default,
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

    def start(self):

        self.status = CommandStatus.RUNNING

    # ---------------------------- #

    def complete(self):

        self.status = CommandStatus.COMPLETED

    # ---------------------------- #

    def fail(self):

        self.status = CommandStatus.FAILED

    # ---------------------------- #

    def is_completed(self):

        return (
            self.status
            == CommandStatus.COMPLETED
        )

    # ---------------------------- #

    def to_dict(self):

        return {

            "command_id": self.command_id,

            "name": self.name,

            "description": self.description,

            "parameters": self.parameters,

            "metadata": self.metadata,

            "status": self.status.value,

            "created_at": self.created_at,

        }

    # ---------------------------- #

    @classmethod
    def from_dict(
        cls,
        data: dict,
    ):

        obj = cls(

            name=data["name"],

            description=data.get(
                "description",
                "",
            ),

            parameters=data.get(
                "parameters",
                {},
            ),

            metadata=data.get(
                "metadata",
                {},
            ),

        )

        obj.command_id = data.get(
            "command_id",
            obj.command_id,
        )

        obj.status = CommandStatus(
            data.get(
                "status",
                "pending",
            )
        )

        obj.created_at = data.get(
            "created_at",
            obj.created_at,
        )

        return obj

    # ---------------------------- #

    def __repr__(self):

        return (
            f"<Command "
            f"{self.name} "
            f"({self.status.value})>"
        )
