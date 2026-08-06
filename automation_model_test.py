from automation.automation_types import Automation


auto = Automation(
    name="Morning Reminder",
    description="Runs every morning.",
    trigger={
        "type": "time",
        "time": "09:00"
    },
    action={
        "type": "command",
        "command": "good morning"
    }
)

print(auto)

print(auto.to_dict())

auto.disable()

print(auto.status)

auto.enable()

print(auto.status)

loaded = Automation.from_dict(
    auto.to_dict()
)

print(loaded)

print(loaded.validate())
