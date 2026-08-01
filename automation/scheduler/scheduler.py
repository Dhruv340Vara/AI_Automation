from __future__ import annotations
import threading
import time
from typing import Dict
from automation.scheduler.scheduled_task import (
    ScheduledTask,
    ScheduleStatus,
)
from automation.scheduler.scheduler_types import (
    ExecutionResult,
)

class Scheduler:
    def __init__(self):
        self._tasks: Dict[str, ScheduledTask] = {}
        self._running = False
        self._thread = None
        self._task_handler = None
        self._poll_interval = 1.0

    def add_task(self, task: ScheduledTask):
        if task.task_id in self._tasks:
            raise ValueError(
                "Task already exists."
            )
        self._tasks[task.task_id] = task
        return task

    def remove_task(self, task_id: str):
        return self._tasks.pop(task_id, None)

    def get_task(self, task_id: str):
        return self._tasks.get(task_id)

    def exists(self, task_id: str):
        return task_id in self._tasks

    def all_tasks(self):
        return list(self._tasks.values())

    def pending_tasks(self):
        return [
            task
            for task in self._tasks.values()
            if task.status == ScheduleStatus.PENDING
        ]

    def paused_tasks(self):
        return [
            task
            for task in self._tasks.values()
            if task.status == ScheduleStatus.PAUSED
        ]

    def running_tasks(self):
        return [
            task
            for task in self._tasks.values()
            if task.status == ScheduleStatus.RUNNING
        ]

    def completed_tasks(self):
        return [
            task
            for task in self._tasks.values()
            if task.status == ScheduleStatus.COMPLETED
        ]

    def cancelled_tasks(self):
        return [
            task
            for task in self._tasks.values()
            if task.status == ScheduleStatus.CANCELLED
        ]

    def count(self):
        return len(self._tasks)

    def clear(self):
        self._tasks.clear()

    def __len__(self):
        return len(self._tasks)

    def __iter__(self):
        return iter(self._tasks.values())

    def __repr__(self):
        return f"<Scheduler tasks={len(self._tasks)}>"

    @property
    def is_running(self):
        return self._running

    def start(self):
        if self._running:
            return False
        self._running = True
        self._thread = threading.Thread(
            target=self._run_loop,
            daemon=True,
        )
        self._thread.start()
        return True

    def _run_loop(self):
        while self._running:
            self._execute_due_tasks()
            time.sleep(self._poll_interval)

    def stop(self):
        if not self._running:
            return False
        self._running = False
        if self._thread is not None:
            self._thread.join(timeout=2)
            self._thread = None
        return True

    def set_poll_interval(self, seconds: float):
        if seconds <= 0:
            raise ValueError(
                "Poll interval must be > 0."
            )
        self._poll_interval = seconds

    def find_due_tasks(self):
        due = []
        for task in self.pending_tasks():
            if task.should_run():
                due.append(task)
        return due

    def _execute_due_tasks(self):
        due_tasks = self.find_due_tasks()
        for task in due_tasks:
            task.mark_running()
            self._dispatch(task)

    def _dispatch(self,task: ScheduledTask):
        try:
            if self._task_handler is None:
                task.mark_completed()
                return
            result = self._task_handler(
                task
            )
            if result is None:
                result = ExecutionResult.SUCCESS
            if result == ExecutionResult.SUCCESS:
                task.mark_completed()
            elif result == ExecutionResult.CANCEL:
                task.cancel()
            elif result == ExecutionResult.RETRY:
                task.resume()
            elif result == ExecutionResult.FAILED:
                task.mark_failed()
            else:
                task.cancel()
        except Exception:
            task.cancel()

    def set_task_handler(self, handler):
         self._task_handler = handler
