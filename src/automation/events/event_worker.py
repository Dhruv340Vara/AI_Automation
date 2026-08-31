from __future__ import annotations

import threading
import time

from automation.events.event_listener import (
    EventListener,
)

from automation.events.event_queue import (
    EventQueue,
)


class EventWorker:
    """
    Background worker that continuously
    processes events from EventQueue.
    """

    def __init__(
        self,
        queue: EventQueue,
        listener: EventListener,
        poll_interval: float = 0.1,
    ):

        self._queue = queue

        self._listener = listener

        self._poll_interval = poll_interval

        self._running = False

        self._thread = None

    # -------------------------------- #

    @property
    def is_running(self):

        return self._running

    # -------------------------------- #

    def start(self):

        if self._running:
            return False

        self._running = True

        self._thread = threading.Thread(

            target=self._run,

            daemon=True,

            name="EventWorker",

        )

        self._thread.start()

        return True

    # -------------------------------- #

    def stop(self):

        if not self._running:
            return False

        self._running = False

        self._thread.join()

        return True

    # -------------------------------- #

    def _run(self):

        while self._running:

            event = self._queue.get(
                timeout=self._poll_interval
            )

            if event is None:
                continue

            try:

                self._listener.listen(
                    event
                )

            finally:

                self._queue.task_done()

    # -------------------------------- #

    def __repr__(self):

        state = (
            "running"
            if self._running
            else "stopped"
        )

        return (
            f"<EventWorker {state}>"
        )
