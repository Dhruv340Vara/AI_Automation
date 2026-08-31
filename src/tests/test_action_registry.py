from automation.actions.action_executor import ActionExecutor

executor = ActionExecutor()

assert executor.registry.exists("print")
assert executor.registry.exists("python_function")
assert executor.registry.exists("shell_command")

assert executor.registry.count() == 3

print("Action Registry OK")
