from automation.automation_core import AutomationCore

core = AutomationCore()

core.clear()

auto = core.create(
    name="Morning Reminder",
    description="Daily reminder",
    trigger={
        "type": "time",
        "time": "09:00"
    },
    action={
        "type": "command",
        "command": "good morning"
    }
)

print(core.count())

print(core.exists(auto.automation_id))

print(core.exists_name("Morning Reminder"))

print(core.get(auto.automation_id))

core.disable(auto.automation_id)

print(
    core.get(auto.automation_id).status
)

core.enable(auto.automation_id)

print(
    core.get(auto.automation_id).status
)

core.update(
    auto.automation_id,
    description="Updated description"
)

print(
    core.get(auto.automation_id).description
)

print(core.list())

core.reload()

print(core.count())

core.delete(auto.automation_id)

print(core.count())
