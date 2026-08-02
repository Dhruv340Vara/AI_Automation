import time

from automation.automation_runtime import AutomationRuntime
from automation.automation_types import Automation

runtime = AutomationRuntime()

runtime.start()

automation = Automation(
    name="Demo",
    trigger={
        "type": "manual"
    },
    action={
        "type": "print",
        "message": "hello"
    }
)

runtime.register(
    automation
)

assert runtime.run_now(
    automation.automation_id
)

time.sleep(1)

runtime.stop()

print("Runtime Execution OK")
