from __future__ import annotations

from automation.scheduler.scheduler import Scheduler
from automation.worker.worker_pool import WorkerPool
from automation.triggers.trigger_engine import TriggerEngine


class AutomationRuntime:

    def __init__(

        self,

        worker_count: int = 2,

        trigger_storage: str = "data/triggers.json",

    ):

        self.scheduler = Scheduler()

        self.worker_pool = WorkerPool(
            size=worker_count
        )

        self.trigger_engine = TriggerEngine(
            storage_path=trigger_storage
        )

        self._running = False

    @property
    def is_running(self):

        return self._running

    def start(self):

        if self._running:

            return False

        self.worker_pool.start()

        self.scheduler.start()

        self._running = True

        return True

    def stop(self):

        if not self._running:

            return False

        self.scheduler.stop()

        self.worker_pool.stop()

        self._running = False

        return True

    def register_trigger(

        self,

        trigger,

    ):

        return self.trigger_engine.register(
            trigger
        )

    def unregister_trigger(

        self,

        trigger_id,

    ):

        return self.trigger_engine.unregister(
            trigger_id
        )

    def triggers(self):

        return self.trigger_engine.all()

    def __repr__(self):

        state = (
            "running"
            if self._running
            else "stopped"
        )

        return (
            f"<AutomationRuntime "
            f"{state}>"
        )
