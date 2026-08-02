from __future__ import annotations

from automation.scheduler.scheduler import Scheduler
from automation.worker.worker_pool import WorkerPool


class AutomationRuntime:

    def __init__(self, workers: int = 2):

        self.scheduler = Scheduler()
        self.worker_pool = WorkerPool(workers)

    def start(self):

        self.worker_pool.start()
        self.scheduler.start()

    def stop(self):

        self.scheduler.stop()
        self.worker_pool.stop()

    def __repr__(self):

        return (
            f"<AutomationRuntime "
            f"workers={self.worker_pool} "
            f"scheduler={self.scheduler}>"
        )
