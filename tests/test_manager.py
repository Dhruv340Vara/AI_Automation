from automation.automation_manager import AutomationManager
from automation.automation_types import Automation


def run():

    manager = AutomationManager()

    auto = Automation(
        name="Demo"
    )

    manager.create_automation(auto)

    assert manager.count() == 1

    assert manager.automation_exists(
        auto.automation_id
    )

    manager.disable_automation(
        auto.automation_id
    )

    manager.enable_automation(
        auto.automation_id
    )

    manager.delete_automation(
        auto.automation_id
    )

    assert manager.count() == 0

    return True
