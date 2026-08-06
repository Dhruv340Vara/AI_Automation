from datetime import datetime, timedelta

from automation.scheduler.scheduler import Scheduler
from automation.scheduler.scheduled_task import (
    ScheduledTask,
    ScheduleType,
)

scheduler = Scheduler()

task = ScheduledTask(

    automation_id="AUTO001",

    schedule_type=ScheduleType.ONCE,

    next_run=datetime.now() + timedelta(seconds=5)
)

scheduler.add_task(task)

print(scheduler)

print(scheduler.count())

print(scheduler.exists(task.task_id))

print(scheduler.get_task(task.task_id))

print(scheduler.pending_tasks())

task.pause()

print(scheduler.paused_tasks())

task.resume()

print(scheduler.pending_tasks())

task.cancel()

print(scheduler.cancelled_tasks())

scheduler.remove_task(task.task_id)

print(scheduler.count())
