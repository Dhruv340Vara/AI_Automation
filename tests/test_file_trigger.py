from automation.triggers import (
    FileTrigger,
)

trigger = FileTrigger(

    name="Downloads",

    path="/storage/emulated/0/Download",

    events=[
        "created",
        "modified",
    ],

    recursive=True,

    extensions=[
        ".pdf",
        ".jpg",
    ],

)

print(trigger)

print(trigger.path)

print(trigger.events)

print(trigger.recursive)

print(
    trigger.allows(
        "test.pdf"
    )
)

print(
    trigger.allows(
        "abc.txt"
    )
)

print(
    trigger.watches(
        "created"
    )
)
