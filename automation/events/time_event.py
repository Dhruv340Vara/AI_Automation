from __future__ import annotations

from datetime import datetime

from automation.events.event import Event
from automation.events.event_types import EventType


class TimeEventFactory:
    """
    Factory for creating time-based events.
    """

    @staticmethod
    def once(run_at: datetime) -> Event:

        return Event(
            event_type=EventType.TIME,
            source="scheduler",
            payload={
                "mode": "once",
                "run_at": run_at.isoformat(),
            },
        )

    @staticmethod
    def interval(seconds: int) -> Event:

        return Event(
            event_type=EventType.INTERVAL,
            source="scheduler",
            payload={
                "mode": "interval",
                "seconds": seconds,
            },
        )

    @staticmethod
    def daily(
        hour: int,
        minute: int = 0,
    ) -> Event:

        return Event(
            event_type=EventType.TIME,
            source="scheduler",
            payload={
                "mode": "daily",
                "hour": hour,
                "minute": minute,
            },
        )

    @staticmethod
    def weekly(
        weekday: int,
        hour: int,
        minute: int = 0,
    ) -> Event:

        return Event(
            event_type=EventType.TIME,
            source="scheduler",
            payload={
                "mode": "weekly",
                "weekday": weekday,
                "hour": hour,
                "minute": minute,
            },
        )

    @staticmethod
    def monthly(
        day: int,
        hour: int,
        minute: int = 0,
    ) -> Event:

        return Event(
            event_type=EventType.TIME,
            source="scheduler",
            payload={
                "mode": "monthly",
                "day": day,
                "hour": hour,
                "minute": minute,
            },
        )
