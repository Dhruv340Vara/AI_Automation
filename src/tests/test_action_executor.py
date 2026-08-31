from automation.actions.action_executor import ActionExecutor
from automation.automation_types import Automation

executor = ActionExecutor()

automation = Automation(
    name="Print Test",
    action={
        "type": "print",
        "message": "Hello AI Assistant"
    }
)

assert executor.execute(
    automation
)

print("Action Executor OK")
