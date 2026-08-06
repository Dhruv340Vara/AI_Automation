from automation.actions.action_executor import ActionExecutor
from automation.automation_types import Automation

executor = ActionExecutor()

automation = Automation(
    name="Shell Test",
    action={
        "type": "shell_command",
        "command": "echo Hello AI Assistant"
    }
)

assert executor.execute(
    automation
)

print(
    "Shell Command Action OK"
)
