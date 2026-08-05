from __future__ import annotations

from enum import Enum


class EventType(Enum):
    """
    Base event types supported by
    the automation framework.

    New event types can be added
    without changing the Event model.
    """

    # ---------------------------------
    # Manual
    # ---------------------------------

    MANUAL = "manual"

    # ---------------------------------
    # Time
    # ---------------------------------

    TIME = "time"
    INTERVAL = "interval"
    SCHEDULE = "schedule"

    # ---------------------------------
    # File System
    # ---------------------------------

    FILE_CREATED = "file_created"
    FILE_DELETED = "file_deleted"
    FILE_MODIFIED = "file_modified"
    FILE_RENAMED = "file_renamed"

    FOLDER_CREATED = "folder_created"
    FOLDER_DELETED = "folder_deleted"

    # ---------------------------------
    # Web
    # ---------------------------------

    WEBHOOK = "webhook"
    API = "api"

    # ---------------------------------
    # Command
    # ---------------------------------

    COMMAND = "command"

    # ---------------------------------
    # Device
    # ---------------------------------

    BATTERY = "battery"
    WIFI = "wifi"
    BLUETOOTH = "bluetooth"
    LOCATION = "location"

    # ---------------------------------
    # Runtime
    # ---------------------------------

    AUTOMATION_STARTED = "automation_started"
    AUTOMATION_COMPLETED = "automation_completed"
    AUTOMATION_FAILED = "automation_failed"

    # ---------------------------------
    # Custom
    # ---------------------------------

    CUSTOM = "custom"

    @classmethod
    def values(cls) -> list[str]:
        """
        Return all event values.
        """

        return [
            event.value
            for event in cls
        ]

    @classmethod
    def exists(
        cls,
        value: str,
    ) -> bool:
        """
        Check whether an event type exists.
        """

        return value in cls.values()

    @classmethod
    def from_string(
        cls,
        value: str,
    ):
        """
        Convert string to EventType.
        """

        for event in cls:

            if event.value == value:

                return event

        raise ValueError(
            f"Unknown event type: {value}"
        )

    def __str__(self):

        return self.value
