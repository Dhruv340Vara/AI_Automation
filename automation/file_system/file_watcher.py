from __future__ import annotations

from pathlib import Path

from watchdog.events import (
    FileSystemEventHandler,
)

from watchdog.observers import Observer

from automation.events.file_event import (
    FileEventFactory,
)


class FileWatcher(FileSystemEventHandler):
    """
    Watches a directory and generates
    file events.
    """

    def __init__(
        self,
        trigger,
        runtime,
    ):

        self.trigger = trigger

        self.runtime = runtime

        self.observer = Observer()

    # -------------------------------- #

    def start(self):

        self.observer.schedule(

            self,

            self.trigger.path,

            recursive=self.trigger.recursive,

        )

        self.observer.start()

    # -------------------------------- #

    def stop(self):

        self.observer.stop()

        self.observer.join()

    # -------------------------------- #

    def _valid(
        self,
        path: str,
    ) -> bool:

        filename = Path(path).name

        return self.trigger.allows(
            filename
        )

    # -------------------------------- #

    def on_created(
        self,
        event,
    ):

        if event.is_directory:
            return

        if not self.trigger.watches(
            "created"
        ):
            return

        if not self._valid(
            event.src_path
        ):
            return

        self.runtime.emit_event(

            FileEventFactory.created(

                event.src_path

            )

        )

    # -------------------------------- #

    def on_modified(
        self,
        event,
    ):

        if event.is_directory:
            return

        if not self.trigger.watches(
            "modified"
        ):
            return

        if not self._valid(
            event.src_path
        ):
            return

        self.runtime.emit_event(

            FileEventFactory.modified(

                event.src_path

            )

        )

    # -------------------------------- #

    def on_deleted(
        self,
        event,
    ):

        if event.is_directory:
            return

        if not self.trigger.watches(
            "deleted"
        ):
            return

        self.runtime.emit_event(

            FileEventFactory.deleted(

                event.src_path

            )

        )

    # -------------------------------- #

    def on_moved(
        self,
        event,
    ):

        if event.is_directory:
            return

        if not self.trigger.watches(
            "renamed"
        ):
            return

        self.runtime.emit_event(

            FileEventFactory.renamed(

                event.src_path,

                event.dest_path,

            )

        )

    # -------------------------------- #

    def __repr__(self):

        return (

            "<FileWatcher "

            f"path={self.trigger.path}>"

        )
