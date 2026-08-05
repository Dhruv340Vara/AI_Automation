from __future__ import annotations

from automation.conditions.condition_evaluator import (ConditionEvaluator,)
from automation.manual.manual_trigger_manager import (ManualTriggerManager,)
from automation.webhook.webhook_server import (WebhookServer,)
from automation.webhook.webhook_request import (WebhookRequest,)
from automation.events import (EventDispatcher,EventListener,EventQueue,EventRegistry,TimeEventGenerator,)
from automation.events import (EventWorker,)
from automation.file_system import (FileWatcher,)
from automation.triggers.trigger_engine import (TriggerEngine,)
from automation.scheduler.scheduled_task import ScheduledTask
from automation.scheduler.scheduler_types import ExecutionResult
from typing import Dict
from automation.api.api_poller import (APIPoller,)
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
        self.scheduler.set_task_handler(self._handle_task)
        self.event_registry = EventRegistry()
        self.event_dispatcher = EventDispatcher(self.event_registry)   
        self.event_listener = EventListener(self.event_dispatcher)
        self.event_queue = EventQueue()
        self.event_worker = EventWorker(self.event_queue,self.event_listener,)
        self._watchers = []
        self.webhook_server = WebhookServer()
        self._api_pollers = []
        self.manual_manager = (ManualTriggerManager(self))
        self.condition_evaluator = (ConditionEvaluator())
        self.trigger_engine = TriggerEngine()
        self.time_event_generator = (TimeEventGenerator())
        self.executor = ActionExecutor()

    def start(self):
        if self.scheduler.is_running:
            return False
        self.worker_pool.start()
        self.event_worker.start()
        self.start_watchers()
        self.start_api_pollers()
        self.scheduler.start()
        return True

    def register_callback(self,automation_id: str):
        self.callbacks.register(automation_id,lambda: self.run_now(automation_id))

    def unregister_callback(self,automation_id: str):
        self.callbacks.unregister(automation_id)

    def stop(self):
        if not self.scheduler.is_running:
            return False
        self.scheduler.stop()
        self.stop_api_pollers()
        self.stop_watchers()
        self.event_worker.stop()
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

    def emit_event(self,event,):
        context = {}
        if hasattr(event,"payload",):
            context = event.payload
        if (self.condition_evaluator.count()> 0):
            if not self.evaluate_conditions(context):
                return False
            self.event_queue.put(event)
            return True

    def generate_time_event(self,trigger,):
        event = (self.time_event_generator.generate(trigger))
        return self.emit_event(
            event
        )

    def register_watcher(self,watcher,):
        self._watchers.append(watcher)
        return watcher


    def unregister_watcher(self,watcher,):
        if watcher in self._watchers:
            self._watchers.remove(watcher)
            return True
        return False


    def start_watchers(self,):
        for watcher in self._watchers:
            watcher.start()


    def stop_watchers(self,):
        for watcher in self._watchers:
            watcher.stop()


    def register_file_trigger(self,trigger,):
        watcher = FileWatcher(trigger,self,)
        self.register_watcher(watcher)
        return watcher

    def register_webhook_trigger(self,trigger,):
        self.webhook_server.register(trigger)
        return trigger

    def unregister_webhook_trigger(self,endpoint: str,):
        self.webhook_server.unregister(endpoint)

    def emit_webhook(self,endpoint: str,method: str = "POST",headers: dict | None = None,body: dict | None = None,remote_addr: str | None = None,):
        request = WebhookRequest(endpoint=endpoint,method=method,headers=headers or {},body=body or {},remote_addr=remote_addr,)
        event = self.webhook_server.handle(request)
        if event is None:
            return False
        return self.emit_event(event)

    def register_api_trigger(self,trigger,):
        poller = APIPoller(trigger,self,)
        self._api_pollers.append(poller)
        return poller

    def unregister_api_trigger(self,poller,):
        if poller in self._api_pollers:
            poller.stop()
            self._api_pollers.remove(poller)
            return True
        return False

    def start_api_pollers(self,):
        for poller in self._api_pollers:
            poller.start()

    def stop_api_pollers(self,):
        for poller in self._api_pollers:
            poller.stop()

    def register_manual_trigger(self,trigger,):
        return (self.manual_manager.register(trigger))

    def unregister_manual_trigger(self,trigger_name: str,):
        return (self.manual_manager.unregister(trigger_name))

    def trigger_manual(self,trigger_name: str,user: str | None = None,metadata: dict | None = None,):
        return (self.manual_manager.trigger(trigger_name=trigger_name,user=user,metadata=metadata,))

    def add_condition(self,condition,):
        return (self.condition_evaluator.add(condition))

    def remove_condition(self,condition,):
        return (self.condition_evaluator.remove(condition))

    def clear_conditions(self,):
        self.condition_evaluator.clear()

    def evaluate_conditions(self,context: dict,):
        return (self.condition_evaluator.evaluate(context))

    def evaluate_condition_details(self,context: dict,):
        return (self.condition_evaluator.evaluate_all(context))
