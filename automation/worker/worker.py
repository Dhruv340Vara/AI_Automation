from __future__ import annotations

import threading
from typing import Optional

from automation.worker.job_queue import JobQueue


class Worker:
    """
    Background worker that continuously
    processes jobs from a JobQueue.
    """

    def __init__(self, name: str = "Worker"):

        self.name = name

        self._thread: Optional[threading.Thread] = None

        self._running = False

        self._queue: Optional[JobQueue] = None

    @property
    def is_running(self) -> bool:

        return self._running

    def start(
        self,
        queue: JobQueue,
    ):

        if self._running:
            return False

        self._queue = queue

        self._running = True

        self._thread = threading.Thread(
            target=self._run,
            daemon=True,
            name=self.name,
        )

        self._thread.start()

        return True

    def _run(self):

        try:

            while self._running:

                job = self._queue.get(timeout=0.5)

                if job is None:
                    continue

                try:

                    job.execute()

                finally:

                    self._queue.task_done()

        finally:

            self._running = False

    def stop(self):

        self._running = False

    def join(
        self,
        timeout: float | None = None,
    ):

        if self._thread is not None:

            self._thread.join(timeout)

    def __repr__(self):

        state = (
            "running"
            if self._running
            else "stopped"
        )

        return f"<Worker {self.name} ({state})>"
