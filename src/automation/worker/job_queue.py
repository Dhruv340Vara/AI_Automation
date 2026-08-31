from __future__ import annotations

from queue import Queue, Empty

from automation.worker.job import Job


class JobQueue:

    def __init__(self):

        self._queue = Queue()

    def put(self, job: Job):

        self._queue.put(job)

    def get(self, timeout=None):

        try:

            return self._queue.get(
                timeout=timeout
            )

        except Empty:

            return None

    def task_done(self):

        self._queue.task_done()

    def join(self):

        self._queue.join()

    def empty(self):

        return self._queue.empty()

    def size(self):

        return self._queue.qsize()

    def clear(self):

        while not self._queue.empty():

            try:

                self._queue.get_nowait()

                self._queue.task_done()

            except Empty:

                break

    def __len__(self):

        return self.size()

    def __repr__(self):

        return f"<JobQueue size={self.size()}>"
