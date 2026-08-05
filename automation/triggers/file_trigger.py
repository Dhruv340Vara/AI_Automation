from __future__ import annotations

from automation.triggers.trigger import Trigger
from automation.triggers.trigger_types import (
    TriggerType,
)


class FileTrigger(Trigger):
    """
    Trigger for file system events.
    """

    def __init__(
        self,
        name: str,
        path: str,
        events: list[str] | None = None,
        recursive: bool = False,
        extensions: list[str] | None = None,
        ignore_hidden: bool = True,
    ):

        metadata = {

            "path": path,

            "events": events or [
                "created"
            ],

            "recursive": recursive,

            "extensions": (
                extensions or []
            ),

            "ignore_hidden": (
                ignore_hidden
            ),
        }

        super().__init__(

            trigger_type=TriggerType.FILE,

            name=name,

            metadata=metadata,

        )

    # -------------------------------- #

    @property
    def path(self):

        return self.metadata["path"]

    @property
    def events(self):

        return self.metadata["events"]

    @property
    def recursive(self):

        return self.metadata[
            "recursive"
        ]

    @property
    def extensions(self):

        return self.metadata[
            "extensions"
        ]

    @property
    def ignore_hidden(self):

        return self.metadata[
            "ignore_hidden"
        ]

    # -------------------------------- #

    def watches(
        self,
        event_name: str,
    ) -> bool:

        return (
            event_name
            in self.events
        )

    # -------------------------------- #

    def allows(
        self,
        filename: str,
    ) -> bool:

        if (
            self.ignore_hidden
            and filename.startswith(".")
        ):
            return False

        if not self.extensions:
            return True

        return any(

            filename.endswith(ext)

            for ext in self.extensions

        )

    # -------------------------------- #

    def __repr__(self):

        return (

            "<FileTrigger "

            f"{self.name} "

            f"path={self.path}>"

        )
