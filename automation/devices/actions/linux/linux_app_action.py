"""
linux_app_action.py

Launch Linux desktop applications.
"""

from __future__ import annotations

import subprocess

from automation.devices.actions.device_action import (
    DeviceAction,
)


class LinuxAppAction(DeviceAction):

    def __init__(self):

        super().__init__(
            "open_app",
        )

    # ---------------------------- #

    def validate(
        self,
        request,
    ):

        app = request.get_parameter(
            "app",
        )

        return bool(app)

    # ---------------------------- #

    def perform(
        self,
        request,
    ):

        app = request.get_parameter(
            "app",
        )

        try:

            subprocess.Popen(
                [app],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

        except FileNotFoundError:

            raise RuntimeError(
                f"Application '{app}' not found."
            )

        return True
