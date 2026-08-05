from __future__ import annotations

from automation.events.event import Event
from automation.events.event_dispatcher import (
    EventDispatcher,
)


class EventListener:
    """
    Receives events and forwards them
    to the dispatcher.
    """

    def __init__(
        self,
        dispatcher: EventDispatcher,
    ):

        self._dispatcher = dispatcher

        self._enabled = True

        self._received = 0

    # -------------------------------------------- #

    @property
    def enabled(self) -> bool:

        return self._enabled

    # -------------------------------------------- #

    @property
    def received_count(self) -> int:

        return self._received

    # -------------------------------------------- #

    def enable(self):

        self._enabled = True

    def disable(self):

        self._enabled = False

    # -------------------------------------------- #

    def listen(
        self,
        event: Event,
    ) -> int:
        """
        Listen for an event and dispatch it.

        Returns:
            Number of executed handlers.
        """

        if not self._enabled:
            return 0

        self._received += 1

        return self._dispatcher.dispatch(
            event
        )

    # -------------------------------------------- #

    def reset(self):

        self._received = 0

    # -------------------------------------------- #

    def __repr__(self):

        state = (
            "enabled"
            if self._enabled
            else "disabled"
        )

        return (
            "<EventListener "
            f"{state} "
            f"received={self._received}>"
        )
