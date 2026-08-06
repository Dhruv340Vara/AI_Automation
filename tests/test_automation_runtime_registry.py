from automation.automation_runtime import AutomationRuntime
from automation.automation_types import Automation

runtime = AutomationRuntime()

automation = Automation(
    name="Demo",
    trigger="manual",
    action="print('hello')"
)

runtime.register(automation)

assert runtime.count() == 1
assert runtime.get(
    automation.automation_id
) is automation

print(runtime.list_automations())

runtime.unregister(
    automation.automation_id
)

assert runtime.count() == 0

print("Runtime Registry OK")
