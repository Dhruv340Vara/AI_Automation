"""
device_action_registry.py

Registry for device actions.
"""

from __future__ import annotations

from automation.devices.actions.device_action import (
    DeviceAction,
)


class DeviceActionRegistry:

    def __init__(self):

        self._actions: dict[
            str,
            DeviceAction,
        ] = {}

    # -------------------------------- #

    def register(
        self,
        action: DeviceAction,
    ):

        self._actions[
            action.name.lower()
        ] = action

    # -------------------------------- #

    def unregister(
        self,
        name: str,
    ):

        self._actions.pop(
            name.lower(),
            None,
        )

    # -------------------------------- #

    def get(
        self,
        name: str,
    ):

        return self._actions.get(
            name.lower()
        )

    # -------------------------------- #

    def exists(
        self,
        name: str,
    ) -> bool:

        return (
            name.lower()
            in self._actions
        )

    # -------------------------------- #

    def actions(
        self,
    ):

        return sorted(
            self._actions.keys()
        )

    # -------------------------------- #

    def count(
        self,
    ):

        return len(
            self._actions
        )

    # -------------------------------- #

    def clear(
        self,
    ):

        self._actions.clear()

    # -------------------------------- #

    def execute(
        self,
        request,
    ):

        action = self.get(
            request.action
        )

        if action is None:

            raise ValueError(

                f"Unknown device action: {request.action}"

            )

        return action.execute(
            request
        )

    # -------------------------------- #

    def __len__(
        self,
    ):

        return self.count()

    # -------------------------------- #

    def __repr__(
        self,
    ):

        return (
            "<DeviceActionRegistry "
            f"actions={self.count()}>"
        )
