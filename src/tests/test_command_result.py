from automation.devices import (
    CommandResult,
)

result = CommandResult(

    success=True,

    stdout="Hello",

    stderr="",

    returncode=0,

    execution_time=0.012,

)

print(result)

print()

print(result.success)

print()

print(result.failed)

print()

print(bool(result))

print()

print(result.to_dict())
