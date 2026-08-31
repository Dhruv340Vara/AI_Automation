from automation.triggers.manual_trigger import (
    ManualTrigger,
)

trigger = ManualTrigger(

    name="Run Backup",

    description="Run backup manually",

)

print(trigger)

print(trigger.name)

print(trigger.description)

print(trigger.activate())
