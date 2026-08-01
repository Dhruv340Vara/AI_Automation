from datetime import datetime

from automation.scheduler.scheduler import Scheduler

from automation.scheduler.scheduled_task import (
    ScheduledTask,
    ScheduleType,
)

scheduler = Scheduler()

task = ScheduledTask(

    automation_id="AUTO001",

    schedule_type=ScheduleType.MONTHLY,

    next_run=datetime(2026, 1, 31, 10, 0),

    day=31,
)

task.last_run = datetime(
    2026,
    1,
    31,
    10,
    0,
)

scheduler._reschedule_task(task)

print(task.next_run)
