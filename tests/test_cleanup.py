from datetime import datetime
from automation.scheduler.scheduler import Scheduler
from automation.scheduler.scheduled_task import (
    ScheduledTask,
    ScheduleType,
)

def run():
    scheduler = Scheduler()
    task = ScheduledTask(
        automation_id="AUTO001",
        schedule_type=ScheduleType.ONCE,
        next_run=datetime.now(),
    )
    task.mark_completed()
    scheduler.add_task(task)
    print(scheduler.count())
    removed = scheduler.cleanup()
    print(removed)
    print(scheduler.count())

if __name__ == "__main__":
    run()
