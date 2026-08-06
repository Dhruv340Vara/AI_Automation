from __future__ import annotations

from collections.abc import Callable

from automation.events.event_types import EventType


class EventRegistry:
    """
    Stores event handlers.

    One EventType can have multiple handlers.
    """

    def __init__(self):

        self._handlers: dict[
            EventType,
            list[Callable]
        ] = {}

    # ------------------------------------------------ #

    def register(
        self,
        event_type: EventType,
        handler: Callable,
    ) -> None:

        if not isinstance(
            event_type,
            EventType,
        ):
            raise TypeError(
                "event_type must be EventType."
            )

        if not callable(handler):
            raise TypeError(
                "handler must be callable."
            )

        handlers = self._handlers.setdefault(
            event_type,
            []
        )

        if handler not in handlers:
            handlers.append(handler)

    # ------------------------------------------------ #

    def unregister(
        self,
        event_type: EventType,
        handler: Callable,
    ) -> bool:

        handlers = self._handlers.get(
            event_type
        )

        if handlers is None:
            return False

        if handler not in handlers:
            return False

        handlers.remove(handler)

        if not handlers:
            del self._handlers[event_type]

        return True

    # ------------------------------------------------ #

    def get_handlers(
        self,
        event_type: EventType,
    ) -> list[Callable]:

        return list(
            self._handlers.get(
                event_type,
                [],
            )
        )

    # ------------------------------------------------ #

    def has_handlers(
        self,
        event_type: EventType,
    ) -> bool:

        return (
            len(
                self._handlers.get(
                    event_type,
                    [],
                )
            )
            > 0
        )

    # ------------------------------------------------ #

    def clear(self):

        self._handlers.clear()

    # ------------------------------------------------ #

    def event_count(self):

        return len(
            self._handlers
        )

    def handler_count(self):

        return sum(
            len(handlers)
            for handlers
            in self._handlers.values()
        )

    # ------------------------------------------------ #

    def registered_events(self):

        return list(
            self._handlers.keys()
        )

    # ------------------------------------------------ #

    def __contains__(
        self,
        event_type: EventType,
    ):

        return self.has_handlers(
            event_type
        )

    def __len__(self):

        return self.handler_count()

    def __repr__(self):

        return (
            "<EventRegistry "
            f"events={self.event_count()} "
            f"handlers={self.handler_count()}>"
        )
