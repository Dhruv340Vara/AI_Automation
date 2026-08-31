from datetime import datetime

from automation.automation_runtime import (
    AutomationRuntime,
)

from automation.events import (
    EventType,
)

from automation.triggers import (
    TimeTrigger,
)

runtime = AutomationRuntime()

def on_time(event):

    print(
        "Time Event:",
        event.event_type.value
    )

runtime.event_registry.register(
    EventType.TIME,
    on_time,
)

trigger = TimeTrigger(
    name="Morning",
    schedule_type="once",
    run_at=datetime.now(),
)

runtime.generate_time_event(
    trigger
)

print("Runtime OK")
