from __future__ import annotations

from automation.events.event import Event
from automation.events.event_types import EventType


class ManualEventFactory:
    """
    Factory for creating manual trigger events.
    """

    @staticmethod
    def trigger(
        trigger_name: str,
        source: str = "manual",
        user: str | None = None,
        metadata: dict | None = None,
    ) -> Event:

        return Event(
            event_type=EventType.MANUAL,
            source=source,
            payload={
                "trigger": trigger_name,
                "user": user,
                "metadata": metadata or {},
            },
        )

    @staticmethod
    def button(
        button_id: str,
        user: str | None = None,
    ) -> Event:

        return Event(
            event_type=EventType.MANUAL,
            source="button",
            payload={
                "button": button_id,
                "user": user,
            },
        )

    @staticmethod
    def cli(
        command: str,
    ) -> Event:

        return Event(
            event_type=EventType.MANUAL,
            source="cli",
            payload={
                "command": command,
            },
        )

    @staticmethod
    def voice(
        command: str,
        confidence: float | None = None,
    ) -> Event:

        return Event(
            event_type=EventType.MANUAL,
            source="voice",
            payload={
                "command": command,
                "confidence": confidence,
            },
        )

    @staticmethod
    def custom(
        source: str,
        payload: dict,
    ) -> Event:

        return Event(
            event_type=EventType.MANUAL,
            source=source,
            payload=payload,
        )
