"""
device_action.py

Base class for every device action.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from automation.devices.device_request import (
    DeviceRequest,
)


class DeviceAction(ABC):

    def __init__(
        self,
        name: str,
    ):

        self.name = name

        self.enabled = True

    # -------------------------------- #

    def enable(self):

        self.enabled = True

    # -------------------------------- #

    def disable(self):

        self.enabled = False

    # -------------------------------- #

    def is_enabled(
        self,
    ) -> bool:

        return self.enabled

    # -------------------------------- #

    def validate(
        self,
        request: DeviceRequest,
    ) -> bool:

        return True

    # -------------------------------- #

    def execute(
        self,
        request: DeviceRequest,
    ):

        if not self.enabled:

            raise RuntimeError(
                f"{self.name} action is disabled."
            )

        if not self.validate(
            request,
        ):

            raise ValueError(
                "Invalid device request."
            )

        return self.perform(
            request,
        )

    # -------------------------------- #

    @abstractmethod
    def perform(
        self,
        request: DeviceRequest,
    ):
        """
        Execute the actual device action.
        """

    # -------------------------------- #

    def __repr__(self):

        state = (
            "enabled"
            if self.enabled
            else "disabled"
        )

        return (
            f"<DeviceAction "
            f"{self.name} "
            f"({state})>"
        )
