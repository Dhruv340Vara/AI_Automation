from automation.automation_runtime import AutomationRuntime
from automation.automation_types import Automation

runtime = AutomationRuntime()

automation = Automation(
    name="Demo",
    trigger={
        "type": "manual"
    },
    action={
        "type": "print"
    }
)

runtime.register(
    automation
)

assert runtime.callbacks.exists(
    automation.automation_id
)

print(
    runtime.callbacks.count()
)

runtime.unregister(
    automation.automation_id
)

assert runtime.callbacks.count() == 0

print(
    "Runtime Callback OK"
)
