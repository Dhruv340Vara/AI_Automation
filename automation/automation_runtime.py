from __future__ import annotations
from typing import Dict
from automation.automation_types import Automation
from automation.scheduler.scheduler import Scheduler
from automation.worker.worker_pool import WorkerPool
from automation.worker.job import Job

class AutomationRuntime:

    def __init__(self, workers: int = 2):
        self.scheduler = Scheduler()
        self.worker_pool = WorkerPool(workers)
        self._automations: Dict[str, Automation] = {}

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

    def register(self, automation: Automation):
        self._automations[
            automation.automation_id
        ] = automation

    def unregister(
        self,
        automation_id: str
    ) -> bool:
        return (
            self._automations.pop(
                automation_id,
                None
            )
            is not None
        )

    def get(
        self,
        automation_id: str
    ):
        return self._automations.get(
            automation_id
        )

    def list_automations(self):
        return list(
            self._automations.values()
        )

    def count(self):
        return len(
            self._automations
        )

    def run_now(
        self,
        automation_id: str
    ) -> bool:

        automation = self.get(
            automation_id
        )

        if automation is None:
            return False

        if not automation.is_enabled():
            return False

        def execute():

            print(
                f"[Runtime] Executing: "
                f"{automation.name}"
            )

        job = Job(
            execute
        )

        self.worker_pool.submit(
            job
        )

        return True
