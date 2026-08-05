from __future__ import annotations
from automation.events import (
    EventDispatcher,
    EventListener,
    EventQueue,
    EventRegistry,
    TimeEventGenerator,
)

from automation.triggers.trigger_engine import (
    TriggerEngine,
)
from automation.scheduler.scheduled_task import ScheduledTask
from automation.scheduler.scheduler_types import ExecutionResult
from typing import Dict
from automation.automation_types import Automation
from automation.scheduler.scheduler import Scheduler
from automation.worker.worker_pool import WorkerPool
from automation.worker.job import Job
from automation.runtime_callbacks import RuntimeCallbacks
from automation.actions.action_executor import ActionExecutor

class AutomationRuntime:

    def __init__(self, workers: int = 2):
        self.scheduler = Scheduler()
        self.worker_pool = WorkerPool(workers)
        self._automations: Dict[str, Automation] = {}
        self.callbacks = RuntimeCallbacks()
        self.scheduler.set_task_handler(
            self._handle_task
        )
        self.event_registry = EventRegistry()

        self.event_dispatcher = EventDispatcher(
            self.event_registry
        )   

        self.event_listener = EventListener(
            self.event_dispatcher
        )

        self.event_queue = EventQueue()

        self.trigger_engine = TriggerEngine()

        self.time_event_generator = (
            TimeEventGenerator()
        )
        self.executor = ActionExecutor()

    def start(self):
        if self.scheduler.is_running:
            return False
        self.worker_pool.start()
        self.scheduler.start()
        return True

    def register_callback(
        self,
        automation_id: str
    ):

        self.callbacks.register(
            automation_id,
            lambda: self.run_now(
                automation_id
            )
        )

    def unregister_callback(
        self,
        automation_id: str
    ):

        self.callbacks.unregister(
            automation_id
        )

    def stop(self):
        if not self.scheduler.is_running:
            return False
        self.scheduler.stop()
        self.worker_pool.stop()
        return True

    def __repr__(self):
        return (
            f"<AutomationRuntime "
            f"workers={self.worker_pool} "
            f"scheduler={self.scheduler}>"
        )

    def register(self,automation: Automation):
        self._automations[automation.automation_id] = automation
        self.register_callback(automation.automation_id)

    def unregister(self,automation_id: str) -> bool:
        self.unregister_callback(automation_id)
        return (self._automations.pop(automation_id,None) is not None)

    def get(self,automation_id: str):
        return self._automations.get(automation_id)

    def list_automations(self):
        return list(self._automations.values())

    def count(self):
        return len(self._automations)

    def run_now(self,automation_id: str) -> bool:
        automation = self.get(automation_id)
        if automation is None:
            return False
        if not automation.is_enabled():
            return False

        def execute():
            print(
                f"[Runtime] Executing: "
                f"{automation.name}"
            )
            self.executor.execute(automation)
        job = Job(execute)
        self.worker_pool.submit(job)
        return True

    def _handle_task(self,task: ScheduledTask):
        if not self.run_now(task.automation_id):
            return ExecutionResult.FAILED
        return ExecutionResult.SUCCESS

    def schedule(self,task: ScheduledTask):
        automation = self.get(task.automation_id)
        if automation is None:
            raise ValueError("Automation not registered.")
        self.scheduler.add_task(task)
        return task

    def emit_event(
        self,
        event,
    ):
        """
        Emit an event into
        the runtime.
        """

        self.event_queue.put(
            event
        )

        queued = self.event_queue.get()

        if queued is None:
            return False

        self.event_listener.listen(
            queued
        )

        self.event_queue.task_done()

        return True

    def generate_time_event(
        self,
        trigger,
    ):

        event = (
            self.time_event_generator.generate(
                trigger
            )
        )

        return self.emit_event(
            event
        )
