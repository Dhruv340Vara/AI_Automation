from datetime import datetime

from automation.scheduler.scheduler import Scheduler

from automation.scheduler.scheduled_task import (
    ScheduledTask,
    ScheduleType,
)

from automation.scheduler.scheduler_types import (
    ExecutionResult,
)


scheduler = Scheduler()


def handler(task):

    return ExecutionResult.SUCCESS


scheduler.set_task_handler(handler)


task = ScheduledTask(

    automation_id="AUTO001",

    schedule_type=ScheduleType.INTERVAL,

    interval=60,

    next_run=datetime.now(),
)

scheduler.add_task(task)

scheduler._execute_due_tasks()

print(task.status)

print(task.next_run)
