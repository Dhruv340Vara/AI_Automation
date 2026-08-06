"""
android_device.py

Android device implementation.
"""

from __future__ import annotations

from automation.devices.device import Device
from automation.devices.device_request import (
    DeviceRequest,
)


class AndroidDevice(Device):

    def __init__(self):

        super().__init__(
            "Android",
        )

    # ---------------------------- #

    def supports(
        self,
        request: DeviceRequest,
    ) -> bool:

        return True

    # ---------------------------- #

    def execute(
        self,
        request: DeviceRequest,
    ):

        if not self.is_enabled():

            raise RuntimeError(
                "Android device is disabled."
            )

        print()

        print("ANDROID DEVICE")

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
            "Waiting for Android Bridge..."
        )

        return True

    # ---------------------------- #

    def __repr__(self):

        state = (
            "enabled"
            if self.enabled
            else "disabled"
        )

        return (
            f"<AndroidDevice "
            f"({state})>"
        )
