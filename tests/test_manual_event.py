from automation.events.manual_event import (
    ManualEventFactory,
)

event = ManualEventFactory.trigger(
    trigger_name="Backup",
    user="Dhruv",
)

print(event)

print(event.event_type.value)

print(event.payload)

print("-" * 50)

event = ManualEventFactory.button(
    button_id="btn_run",
)

print(event.payload)

print("-" * 50)

event = ManualEventFactory.cli(
    command="backup --all",
)

print(event.payload)

print("-" * 50)

event = ManualEventFactory.voice(
    command="Run Backup",
    confidence=0.98,
)

print(event.payload)
