from __future__ import annotations
import threading
from typing import Dict
import calendar
from datetime import datetime, timedelta
from automation.scheduler.timer import Timer
from automation.scheduler.scheduled_task import (
    ScheduledTask,
    ScheduleStatus,
    ScheduleType,
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
        self._timer = Timer()
        self._lock = threading.RLock()
        self._poll_interval = 1.0

    def add_task(self, task: ScheduledTask):
        with self._lock:
            if task.task_id in self._tasks:
                raise ValueError("Task already exists.")
            self._tasks[task.task_id] = task
        return task

    def remove_task(self, task_id: str):
        with self._lock:
            return self._tasks.pop(task_id, None)

    def get_task(self, task_id: str):
        with self._lock:
            return self._tasks.get(task_id)

    def exists(self, task_id: str):
        with self._lock:
            return task_id in self._tasks

    def all_tasks(self):
        with self._lock:
            return list(self._tasks.values())

    def pending_tasks(self):
        with self._lock:
            return [
                task
                for task in self._tasks.values()
                if task.status == ScheduleStatus.PENDING
            ]

    def paused_tasks(self):
        with self._lock:
            return [
                task
                for task in self._tasks.values()
                if task.status == ScheduleStatus.PAUSED
            ]

    def running_tasks(self):
        with self._lock:
            return [
                task
                for task in self._tasks.values()
                if task.status == ScheduleStatus.RUNNING
            ]

    def completed_tasks(self):
        with self._lock:
            return [
                task
                for task in self._tasks.values()
                if task.status == ScheduleStatus.COMPLETED
            ]

    def cancelled_tasks(self):
        with self._lock:
            return [
                task
                for task in self._tasks.values()
                if task.status == ScheduleStatus.CANCELLED
            ]

    def count(self):
        with self._lock:
            return len(self._tasks)

    def clear(self):
        with self._lock:
            self._tasks.clear()

    def cleanup(self):
        with self._lock:
            remove = []
            for task in self._tasks.values():
                if task.status in (
                    ScheduleStatus.COMPLETED,
                    ScheduleStatus.CANCELLED,
                    ScheduleStatus.FAILED,
                ):
                    if task.schedule_type == ScheduleType.ONCE:
                        remove.append(task.task_id)
            for task_id in remove:
                del self._tasks[task_id]
            return len(remove)

    def __len__(self):
        with self._lock:
            return len(self._tasks)

    def __iter__(self):
        with self._lock:
            return iter(list(self._tasks.values()))

    def __repr__(self):
        with self._lock:
            return f"<Scheduler tasks={len(self._tasks)}>"

    @property
    def is_running(self):
        return self._running

    def start(self):
        with self._lock:
            self._timer.reset()
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
            self.cleanup()
            if not self._timer.wait(self._poll_interval):
                break
            
    def stop(self):
        with self._lock:
            if not self._running:
                return False
            self._running = False
            self._timer.stop()
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
        with self._lock:
            tasks = list(
                self._tasks.values()
            )
        due = []

        for task in tasks:
            if (
                task.status == ScheduleStatus.PENDING
                and task.should_run()
            ):
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
                self._reschedule_task(task)
                return
            result = self._task_handler(
                task
            )
            if result is None:
                result = ExecutionResult.SUCCESS
            if result == ExecutionResult.SUCCESS:
                task.mark_completed()
                self._reschedule_task(task)
            elif result == ExecutionResult.CANCEL:
                task.cancel()
            elif result == ExecutionResult.RETRY:
                task.resume()
            elif result == ExecutionResult.FAILED:
                task.mark_failed()
            else:
                task.cancel()
        except Exception as exc:
            print(
                f"Scheduler Error: {exc}"
            )
        task.cancel()

    def set_task_handler(self, handler):
        self._task_handler = handler

    def _next_monthly_run(self,task: ScheduledTask):
        current = task.last_run
        year = current.year
        month = current.month + 1
        if month > 12:
            month = 1
            year += 1
        max_day = calendar.monthrange(
            year,
            month
        )[1]
        day = min(
            task.day,
            max_day
        )
        return datetime(year,month,day,current.hour,current.minute,current.second,current.microsecond)

    def _reschedule_task(self,task: ScheduledTask):
        if task.schedule_type == ScheduleType.ONCE:
            return False
        if task.schedule_type == ScheduleType.INTERVAL:
            task.next_run = (task.last_run +timedelta(seconds=task.interval))
        elif task.schedule_type == ScheduleType.DAILY:
            task.next_run = (task.last_run +timedelta(days=1))
        elif task.schedule_type == ScheduleType.WEEKLY:
            task.next_run = (task.last_run +timedelta(days=7))
        elif task.schedule_type == ScheduleType.MONTHLY:
            task.next_run = (self._next_monthly_run(task))
        task.resume()
        return True
