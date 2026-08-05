from __future__ import annotations

from automation.events.manual_event import (
    ManualEventFactory,
)


class ManualTriggerManager:
    """
    Handles manual trigger execution.
    """

    def __init__(
        self,
        runtime,
    ):

        self.runtime = runtime

        self._triggers = {}

    # -------------------------------- #

    def register(
        self,
        trigger,
    ):

        self._triggers[
            trigger.name
        ] = trigger

        return trigger

    # -------------------------------- #

    def unregister(
        self,
        trigger_name: str,
    ):

        return (
            self._triggers.pop(
                trigger_name,
                None,
            )
            is not None
        )

    # -------------------------------- #

    def exists(
        self,
        trigger_name: str,
    ):

        return (
            trigger_name
            in self._triggers
        )

    # -------------------------------- #

    def get(
        self,
        trigger_name: str,
    ):

        return self._triggers.get(
            trigger_name
        )

    # -------------------------------- #

    def trigger(
        self,
        trigger_name: str,
        user: str | None = None,
        metadata: dict | None = None,
    ):

        trigger = self.get(
            trigger_name
        )

        if trigger is None:
            return False

        event = (
            ManualEventFactory.trigger(
                trigger_name=trigger.name,
                user=user,
                metadata=metadata,
            )
        )

        self.runtime.emit_event(
            event
        )

        return True

    # -------------------------------- #

    def count(self):

        return len(
            self._triggers
        )

    # -------------------------------- #

    def clear(self):

        self._triggers.clear()

    # -------------------------------- #

    def __repr__(self):

        return (
            "<ManualTriggerManager "
            f"triggers={self.count()}>"
        )
