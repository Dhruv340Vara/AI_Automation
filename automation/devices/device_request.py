"""
device_request.py

Represents a request sent to a device.
"""

from __future__ import annotations

from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from typing import Any
from uuid import uuid4


@dataclass
class DeviceRequest:

    action: str

    parameters: dict[str, Any] = field(
        default_factory=dict
    )

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    request_id: str = field(
        default_factory=lambda: str(uuid4())
    )

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

    def to_dict(self):

        return {

            "request_id": self.request_id,

            "action": self.action,

            "parameters": self.parameters,

            "metadata": self.metadata,

            "created_at": self.created_at,

        }

    # ---------------------------- #

    @classmethod
    def from_dict(
        cls,
        data: dict,
    ):

        request = cls(

            action=data["action"],

            parameters=data.get(
                "parameters",
                {},
            ),

            metadata=data.get(
                "metadata",
                {},
            ),

        )

        request.request_id = data.get(
            "request_id",
            request.request_id,
        )

        request.created_at = data.get(
            "created_at",
            request.created_at,
        )

        return request

    # ---------------------------- #

    def __repr__(self):

        return (

            "<DeviceRequest "

            f"{self.action}>"

        )
