from automation.automation_types import Automation


def run():

    auto = Automation(
        name="Morning"
    )

    auto.validate()

    auto.disable()

    assert auto.status.value == "disabled"

    auto.enable()

    assert auto.status.value == "enabled"

    assert auto.name == "Morning"

    return True
