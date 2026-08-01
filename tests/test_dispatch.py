from datetime import datetime

from automation.scheduler.scheduler import Scheduler
from automation.scheduler.scheduled_task import (
    ScheduledTask,
    ScheduleType,
)


scheduler = Scheduler()


def handler(task):

    print("Executing:", task.automation_id)


scheduler.set_task_handler(handler)


task = ScheduledTask(
    automation_id="AUTO001",
    schedule_type=ScheduleType.ONCE,
    next_run=datetime.now(),
)

scheduler.add_task(task)

scheduler._execute_due_tasks()

print(task.status)
