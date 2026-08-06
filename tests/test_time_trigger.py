from datetime import datetime

from automation.triggers import (
    TimeTrigger,
)

trigger = TimeTrigger(
    name="Daily Backup",
    schedule_type="once",
    run_at=datetime.now(),
)

print(trigger)

print(trigger.schedule_type)

print(trigger.run_at)

print(trigger.trigger_type.value)
