from __future__ import annotations

from typing import Any


class ToolArgumentValidator:
    """
    Validates arguments before a tool is executed.
    """

    @staticmethod
    def validate(
        arguments: dict[str, Any],
        schema: dict[str, Any],
    ) -> tuple[bool, str]:
        if not isinstance(arguments, dict):
            return False, "Tool arguments must be a dictionary"

        if not isinstance(schema, dict):
            return False, "Tool schema must be a dictionary"

        parameters = schema.get("parameters", {})

        if not isinstance(parameters, dict):
            return False, "Tool parameters schema must be a dictionary"

        required = parameters.get("required", [])

        if not isinstance(required, list):
            return False, "Required parameters must be a list"

        for name in required:
            if name not in arguments:
                return False, f"Missing required argument: {name}"

        properties = parameters.get("properties", {})

        if not isinstance(properties, dict):
            return False, "Tool properties schema must be a dictionary"

        for name, value in arguments.items():

            if name not in properties:
                return False, f"Unknown argument: {name}"

            expected_type = properties[name].get("type")

            if expected_type == "string":
                if not isinstance(value, str):
                    return False, (
                        f"Argument '{name}' must be a string"
                    )

            elif expected_type == "integer":
                if not isinstance(value, int) or isinstance(value, bool):
                    return False, (
                        f"Argument '{name}' must be an integer"
                    )

            elif expected_type == "number":
                if (
                    not isinstance(value, (int, float))
                    or isinstance(value, bool)
                ):
                    return False, (
                        f"Argument '{name}' must be a number"
                    )

            elif expected_type == "boolean":
                if not isinstance(value, bool):
                    return False, (
                        f"Argument '{name}' must be a boolean"
                    )

            elif expected_type == "object":
                if not isinstance(value, dict):
                    return False, (
                        f"Argument '{name}' must be an object"
                    )

            elif expected_type == "array":
                if not isinstance(value, list):
                    return False, (
                        f"Argument '{name}' must be an array"
                    )

        return True, ""
