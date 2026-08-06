"""
device_manager.py

Manages registered devices.
"""

from __future__ import annotations

from automation.devices.device import (
    Device,
)

from automation.devices.device_request import (
    DeviceRequest,
)


class DeviceManager:

    def __init__(self):

        self._devices: dict[
            str,
            Device,
        ] = {}

    # ---------------------------- #

    def register(
        self,
        device: Device,
    ):

        self._devices[
            device.name.lower()
        ] = device

    # ---------------------------- #

    def unregister(
        self,
        name: str,
    ):

        self._devices.pop(
            name.lower(),
            None,
        )

    # ---------------------------- #

    def get(
        self,
        name: str,
    ):

        return self._devices.get(
            name.lower()
        )

    # ---------------------------- #

    def devices(self):

        return list(
            self._devices.keys()
        )

    # ---------------------------- #

    def count(self):

        return len(
            self._devices
        )

    # ---------------------------- #

    def clear(self):

        self._devices.clear()

    # ---------------------------- #

    def execute(
        self,
        device_name: str,
        request: DeviceRequest,
    ):

        device = self.get(
            device_name
        )

        if device is None:

            raise ValueError(

                f"Device '{device_name}' not found."

            )

        if not device.is_enabled():

            raise RuntimeError(

                f"Device '{device_name}' is disabled."

            )

        if not device.supports(
            request
        ):

            raise RuntimeError(

                f"Device '{device_name}' does not support '{request.action}'."

            )

        return device.execute(
            request
        )

    # ---------------------------- #

    def __repr__(self):

        return (

            "<DeviceManager "

            f"devices={self.count()}>"

        )
