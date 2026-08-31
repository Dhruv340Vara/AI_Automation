from automation.automation_storage import AutomationStorage
from automation.automation_types import Automation


def run():

    storage = AutomationStorage(
        "automation/data/test.json"
    )

    storage.clear()

    auto = Automation(
        name="Storage Test"
    )

    storage.save(
        [auto]
    )

    loaded = storage.load()

    assert len(loaded) == 1

    assert loaded[0].name == "Storage Test"

    storage.clear()

    return True
