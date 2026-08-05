from __future__ import annotations

from automation.events.event import Event
from automation.events.event_types import EventType


class FileEventFactory:
    """
    Factory for creating file system events.
    """

    @staticmethod
    def created(path: str) -> Event:

        return Event(
            event_type=EventType.FILE_CREATED,
            source="file_system",
            payload={
                "path": path,
            },
        )

    @staticmethod
    def modified(path: str) -> Event:

        return Event(
            event_type=EventType.FILE_MODIFIED,
            source="file_system",
            payload={
                "path": path,
            },
        )

    @staticmethod
    def deleted(path: str) -> Event:

        return Event(
            event_type=EventType.FILE_DELETED,
            source="file_system",
            payload={
                "path": path,
            },
        )

    @staticmethod
    def renamed(
        old_path: str,
        new_path: str,
    ) -> Event:

        return Event(
            event_type=EventType.FILE_RENAMED,
            source="file_system",
            payload={
                "old_path": old_path,
                "new_path": new_path,
            },
        )
