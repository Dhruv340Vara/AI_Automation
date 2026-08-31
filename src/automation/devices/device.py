"""
device.py

Base class for every supported device.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from automation.devices.device_request import (
    DeviceRequest,
)


class Device(ABC):

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

    def is_enabled(self):

        return self.enabled

    # -------------------------------- #

    def supports(
        self,
        request: DeviceRequest,
    ) -> bool:
        """
        Override if a device supports
        only specific actions.
        """

        return True

    # -------------------------------- #

    @abstractmethod
    def execute(
        self,
        request: DeviceRequest,
    ):
        """
        Execute a device request.
        """

    # -------------------------------- #

    def __repr__(self):

        state = (
            "enabled"
            if self.enabled
            else "disabled"
        )

        return (
            f"<Device "
            f"{self.name} "
            f"({state})>"
        )

