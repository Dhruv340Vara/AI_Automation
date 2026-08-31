"""
linux_device.py

Linux device implementation.
"""

from __future__ import annotations

from automation.devices.device import Device
from automation.devices.device_request import (
    DeviceRequest,
)


class LinuxDevice(Device):

    def __init__(self):

        super().__init__(
            "Linux",
        )

    # -------------------------------- #

    def supports(
        self,
        request: DeviceRequest,
    ) -> bool:

        return True

    # -------------------------------- #

    def execute(
        self,
        request: DeviceRequest,
    ):

        if not self.is_enabled():

            raise RuntimeError(
                "Linux device is disabled."
            )

        print()

        print("LINUX DEVICE")

        print(
            "Action :",
            request.action,
        )

        print(
            "Parameters :",
            request.parameters,
        )

        print()

        print(
            "Waiting for Action Layer..."
        )

        return True

    # -------------------------------- #

    def __repr__(self):

        state = (
            "enabled"
            if self.enabled
            else "disabled"
        )

        return (
            f"<LinuxDevice "
            f"({state})>"
        )
