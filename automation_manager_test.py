from automation.automation_manager import AutomationManager
from automation.automation_types import Automation


manager = AutomationManager()

auto = Automation(
    name="Morning Reminder",
    trigger={
        "type": "time",
        "time": "09:00"
    },
    action={
        "type": "command",
        "command": "good morning"
    }
)

manager.create_automation(auto)

print(manager.count())

print(manager.automation_exists(auto.automation_id))

print(manager.name_exists("Morning Reminder"))

print(manager.get_automation(auto.automation_id))

manager.disable_automation(auto.automation_id)

print(manager.get_automation(auto.automation_id).status)

manager.enable_automation(auto.automation_id)

print(manager.get_automation(auto.automation_id).status)

manager.update_automation(
    auto.automation_id,
    description="Runs every morning."
)

print(
    manager.get_automation(
        auto.automation_id
    ).description
)

print(manager.list_automations())

manager.delete_automation(auto.automation_id)

print(manager.count())
