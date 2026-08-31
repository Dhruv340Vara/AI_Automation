from automation.security.command_validator import (
    CommandValidator
)

validator = CommandValidator()

assert validator.validate(
    "echo Hello"
)

try:

    validator.validate(
        "rm -rf /"
    )

except PermissionError:

    print(
        "Blocked successfully."
    )

print(
    "Command Validator OK"
)
