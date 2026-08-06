from datetime import datetime

from automation.events import (
    TimeEventGenerator,
)

from automation.triggers import (
    TimeTrigger,
)

generator = TimeEventGenerator()

trigger = TimeTrigger(
    name="Morning Task",
    schedule_type="once",
    run_at=datetime.now(),
)

event = generator.generate(
    trigger
)

print(event)

print(event.payload)

print(generator.last_generated)
