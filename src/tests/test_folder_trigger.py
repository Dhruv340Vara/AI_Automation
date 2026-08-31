from automation.triggers import (
    FolderTrigger,
)

trigger = FolderTrigger(

    name="Downloads",

    path="Downloads",

)

print(trigger)

print(trigger.path)

print(trigger.events)

print(trigger.recursive)

print(trigger.watches("created"))

print(trigger.watches("deleted"))
