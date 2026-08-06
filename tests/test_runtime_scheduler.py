import time
from datetime import datetime

from automation.automation_runtime import AutomationRuntime
from automation.automation_types import Automation
from automation.scheduler.scheduled_task import (
    ScheduledTask,
    ScheduleType,
)

runtime = AutomationRuntime()

runtime.start()

automation = Automation(
    name="Scheduled Demo",
    trigger={
        "type": "once"
    },
    action={
        "type": "print",
        "message": "hello"
    }
)

runtime.register(
    automation
)

task = ScheduledTask(
    automation_id=automation.automation_id,
    schedule_type=ScheduleType.ONCE,
    next_run=datetime.now()
)

runtime.schedule(
    task
)

time.sleep(2)

runtime.stop()

print(
    "Runtime Scheduler OK"
)
