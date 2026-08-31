from __future__ import annotations

from automation.events.event import Event
from automation.events.event_types import EventType


class APIEventFactory:
    """
    Factory for creating API events.
    """

    @staticmethod
    def response(
        url: str,
        method: str,
        status_code: int,
        response: dict | None = None,
        headers: dict | None = None,
        elapsed: float | None = None,
    ) -> Event:

        return Event(
            event_type=EventType.API,
            source="api",
            payload={
                "url": url,
                "method": method.upper(),
                "status_code": status_code,
                "response": response or {},
                "headers": headers or {},
                "elapsed": elapsed,
            },
        )

    @staticmethod
    def error(
        url: str,
        method: str,
        error: str,
    ) -> Event:

        return Event(
            event_type=EventType.API,
            source="api",
            payload={
                "url": url,
                "method": method.upper(),
                "error": error,
            },
        )

    @staticmethod
    def timeout(
        url: str,
        timeout: int,
    ) -> Event:

        return Event(
            event_type=EventType.API,
            source="api",
            payload={
                "url": url,
                "timeout": timeout,
                "error": "Request Timeout",
            },
        )
