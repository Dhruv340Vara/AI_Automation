"""
schedule_parser.py

Parses scheduling information into ScheduledTask values.
"""

from __future__ import annotations

from datetime import datetime, timedelta

from automation.scheduler.scheduled_task import ScheduleType


class ScheduleParser:

    @staticmethod
    def once(run_at: datetime):
        return {
            "schedule_type": ScheduleType.ONCE,
            "next_run": run_at,
        }

    @staticmethod
    def after_seconds(seconds: int):
        return {
            "schedule_type": ScheduleType.ONCE,
            "next_run": datetime.now() + timedelta(seconds=seconds),
        }

    @staticmethod
    def after_minutes(minutes: int):
        return {
            "schedule_type": ScheduleType.ONCE,
            "next_run": datetime.now() + timedelta(minutes=minutes),
        }

    @staticmethod
    def after_hours(hours: int):
        return {
            "schedule_type": ScheduleType.ONCE,
            "next_run": datetime.now() + timedelta(hours=hours),
        }

    @staticmethod
    def interval(seconds: int):
        return {
            "schedule_type": ScheduleType.INTERVAL,
            "next_run": datetime.now() + timedelta(seconds=seconds),
            "interval": seconds,
        }

    @staticmethod
    def daily(hour: int, minute: int = 0):

        now = datetime.now()

        run = now.replace(
            hour=hour,
            minute=minute,
            second=0,
            microsecond=0,
        )

        if run <= now:
            run += timedelta(days=1)

        return {
            "schedule_type": ScheduleType.DAILY,
            "next_run": run,
        }

    @staticmethod
    def weekly(weekday: int, hour: int, minute: int = 0):

        now = datetime.now()

        run = now.replace(
            hour=hour,
            minute=minute,
            second=0,
            microsecond=0,
        )

        days = weekday - now.weekday()

        if days < 0:
            days += 7

        if days == 0 and run <= now:
            days = 7

        run += timedelta(days=days)

        return {
            "schedule_type": ScheduleType.WEEKLY,
            "next_run": run,
            "weekday": weekday,
        }

    @staticmethod
    def monthly(day: int, hour: int, minute: int = 0):

        now = datetime.now()

        month = now.month
        year = now.year

        try:
            run = datetime(
                year,
                month,
                day,
                hour,
                minute,
            )
        except ValueError:
            raise ValueError("Invalid day for current month.")

        if run <= now:

            if month == 12:
                month = 1
                year += 1
            else:
                month += 1

            run = datetime(
                year,
                month,
                day,
                hour,
                minute,
            )

        return {
            "schedule_type": ScheduleType.MONTHLY,
            "next_run": run,
            "day": day,
        }
