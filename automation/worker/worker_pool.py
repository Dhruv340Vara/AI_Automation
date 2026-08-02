from __future__ import annotations

from typing import List

from automation.worker.job_queue import JobQueue
from automation.worker.worker import Worker


class WorkerPool:

    def __init__(
        self,
        size: int = 2,
        name: str = "Worker",
    ):

        if size <= 0:
            raise ValueError(
                "Pool size must be greater than zero."
            )

        self._queue = JobQueue()

        self._workers: List[Worker] = []

        for index in range(size):

            worker = Worker(
                f"{name}-{index + 1}"
            )

            self._workers.append(worker)

    @property
    def queue(self):

        return self._queue

    @property
    def workers(self):

        return list(self._workers)

    def start(self):

        for worker in self._workers:

            worker.start(self._queue)

    def stop(self):

        for worker in self._workers:

            worker.stop()

        for worker in self._workers:

            worker.join()

    def submit(self, job):

        self._queue.put(job)

    def size(self):

        return len(self._workers)

    def __repr__(self):

        return (
            f"<WorkerPool workers={self.size()} "
            f"queue={self._queue.size()}>"
        )
