from __future__ import annotations

from datetime import datetime

from automation.events.time_event import (
    TimeEventFactory,
)
from automation.triggers.time_trigger import (
    TimeTrigger,
)


class TimeEventGenerator:
    """
    Generates time events from
    TimeTrigger objects.
    """

    def __init__(self):

        self._last_generated = None

    # -------------------------------------------- #

    @property
    def last_generated(self):

        return self._last_generated

    # -------------------------------------------- #

    def generate(
        self,
        trigger: TimeTrigger,
    ):

        schedule = trigger.schedule_type

        if schedule == "once":

            event = TimeEventFactory.once(
                trigger.run_at
            )

        elif schedule == "interval":

            event = TimeEventFactory.interval(
                trigger.interval
            )

        elif schedule == "daily":

            event = TimeEventFactory.daily(
                trigger.hour,
                trigger.minute,
            )

        elif schedule == "weekly":

            event = TimeEventFactory.weekly(
                trigger.weekday,
                trigger.hour,
                trigger.minute,
            )

        elif schedule == "monthly":

            event = TimeEventFactory.monthly(
                trigger.day,
                trigger.hour,
                trigger.minute,
            )

        else:

            raise ValueError(
                f"Unknown schedule type: {schedule}"
            )

        self._last_generated = datetime.now()

        return event

    # -------------------------------------------- #

    def __repr__(self):

        return (
            "<TimeEventGenerator>"
        )
