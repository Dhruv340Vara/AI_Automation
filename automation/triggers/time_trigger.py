from __future__ import annotations

from datetime import datetime

from automation.triggers.trigger import Trigger
from automation.triggers.trigger_types import (
    TriggerType,
)


class TimeTrigger(Trigger):
    """
    Time based trigger.
    """

    def __init__(
        self,
        name: str,
        schedule_type: str,
        run_at: datetime | None = None,
        interval: int | None = None,
        hour: int | None = None,
        minute: int = 0,
        weekday: int | None = None,
        day: int | None = None,
    ):

        metadata = {
            "schedule_type": schedule_type,
            "run_at": (
                run_at.isoformat()
                if run_at
                else None
            ),
            "interval": interval,
            "hour": hour,
            "minute": minute,
            "weekday": weekday,
            "day": day,
        }

        super().__init__(
            trigger_type=TriggerType.TIME,
            name=name,
            metadata=metadata,
        )

    # -------------------------------- #

    @property
    def schedule_type(self):

        return self.metadata[
            "schedule_type"
        ]

    @property
    def run_at(self):

        value = self.metadata[
            "run_at"
        ]

        if value is None:
            return None

        return datetime.fromisoformat(
            value
        )

    @property
    def interval(self):

        return self.metadata[
            "interval"
        ]

    @property
    def hour(self):

        return self.metadata[
            "hour"
        ]

    @property
    def minute(self):

        return self.metadata[
            "minute"
        ]

    @property
    def weekday(self):

        return self.metadata[
            "weekday"
        ]

    @property
    def day(self):

        return self.metadata[
            "day"
        ]

    # -------------------------------- #

    def __repr__(self):

        return (
            "<TimeTrigger "
            f"{self.name} "
            f"{self.schedule_type}>"
        )
