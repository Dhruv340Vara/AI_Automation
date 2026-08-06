from automation.automation_core import AutomationCore


def run():

    core = AutomationCore(
        "automation/data/core_test.json"
    )

    core.clear()

    auto = core.create(
        name="Core Test"
    )

    assert core.count() == 1

    core.disable(
        auto.automation_id
    )

    core.enable(
        auto.automation_id
    )

    core.delete(
        auto.automation_id
    )

    assert core.count() == 0

    return True
