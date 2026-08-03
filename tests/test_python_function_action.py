from automation.actions.action_executor import ActionExecutor
from automation.automation_types import Automation


def hello(name):

    print(
        f"Hello {name}"
    )


executor = ActionExecutor()

automation = Automation(
    name="Function Test",
    action={
        "type": "python_function",
        "function": hello,
        "args": [
            "Dhruv"
        ]
    }
)

assert executor.execute(
    automation
)

print(
    "Python Function Action OK"
)
