from datetime import datetime, timedelta
import time

from automation.scheduler.scheduler import Scheduler
from automation.scheduler.scheduled_task import (
    ScheduledTask,
    ScheduleType,
)

scheduler = Scheduler()

task = ScheduledTask(

    automation_id="AUTO001",

    schedule_type=ScheduleType.ONCE,

    next_run=datetime.now() + timedelta(seconds=2)
)

scheduler.add_task(task)

print(task.status)

scheduler.start()

time.sleep(4)

scheduler.stop()

print(task.status)
