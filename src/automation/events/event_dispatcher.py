from __future__ import annotations

from automation.events.event import Event
from automation.events.event_registry import EventRegistry


class EventDispatcher:
    """
    Dispatches events to all registered handlers.
    """

    def __init__(
        self,
        registry: EventRegistry,
    ):

        self._registry = registry

    # ------------------------------------------------ #

    @property
    def registry(self):

        return self._registry

    # ------------------------------------------------ #

    def dispatch(
        self,
        event: Event,
    ) -> int:
        """
        Dispatch event to every registered handler.

        Returns:
            Number of executed handlers.
        """

        event.validate()

        handlers = self._registry.get_handlers(
            event.event_type
        )

        if not handlers:
            return 0

        event.dispatch()

        executed = 0

        try:

            for handler in handlers:

                handler(event)

                executed += 1

            event.complete()

        except Exception:

            event.fail()

            raise

        return executed

    # ------------------------------------------------ #

    def has_handlers(
        self,
        event: Event,
    ) -> bool:

        return self._registry.has_handlers(
            event.event_type
        )

    # ------------------------------------------------ #

    def handler_count(
        self,
        event: Event,
    ) -> int:

        return len(
            self._registry.get_handlers(
                event.event_type
            )
        )

    # ------------------------------------------------ #

    def __repr__(self):

        return (
            "<EventDispatcher "
            f"handlers={self._registry.handler_count()}>"
        )
