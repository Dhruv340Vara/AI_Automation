from datetime import datetime, timedelta

from automation.scheduler.scheduled_task import (
    ScheduledTask,
    ScheduleType,
)


task = ScheduledTask(

    automation_id="AUTO001",

    schedule_type=ScheduleType.ONCE,

    next_run=datetime.now() + timedelta(seconds=2)
)

print(task)

print(task.should_run())

task.pause()

print(task.status)

task.resume()

print(task.status)

data = task.to_dict()

loaded = ScheduledTask.from_dict(data)

print(loaded)

print(loaded.to_dict())
