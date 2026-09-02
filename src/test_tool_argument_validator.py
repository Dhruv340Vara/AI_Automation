from automation.ai.tool_argument_validator import ToolArgumentValidator


def main():
    print("=== Tool Argument Validator Test ===")

    schema = {
        "parameters": {
            "required": ["command"],
            "properties": {
                "command": {
                    "type": "string",
                },
            },
        },
    }

    # 1. Valid arguments
    valid, error = ToolArgumentValidator.validate(
        {"command": "pwd"},
        schema,
    )

    assert valid
    assert error == ""

    print("[PASS] Valid arguments accepted")

    # 2. Missing required argument
    valid, error = ToolArgumentValidator.validate(
        {},
        schema,
    )

    assert not valid
    assert "Missing required argument" in error

    print("[PASS] Missing required argument rejected")

    # 3. Wrong type
    valid, error = ToolArgumentValidator.validate(
        {"command": 123},
        schema,
    )

    assert not valid
    assert "must be a string" in error

    print("[PASS] Wrong argument type rejected")

    # 4. Unknown argument
    valid, error = ToolArgumentValidator.validate(
        {
            "command": "pwd",
            "unknown": "value",
        },
        schema,
    )

    assert not valid
    assert "Unknown argument" in error

    print("[PASS] Unknown argument rejected")

    print("\nTOOL ARGUMENT VALIDATOR TEST PASSED")


if __name__ == "__main__":
    main()
