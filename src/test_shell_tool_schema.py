from automation.ai.tools.shell_tool import ShellTool


def main():
    print("=== Shell Tool Schema Test ===")

    tool = ShellTool()
    schema = tool.schema()

    print("Schema:")
    print(schema)

    assert schema["name"] == "Shell"
    assert "description" in schema
    assert "parameters" in schema

    parameters = schema["parameters"]

    assert parameters["type"] == "object"

    properties = parameters["properties"]

    assert properties["command"]["type"] == "string"
    assert properties["cwd"]["type"] == "string"
    assert properties["timeout"]["type"] == "integer"

    assert "command" in parameters["required"]

    print("[PASS] Tool name")
    print("[PASS] Tool description")
    print("[PASS] Parameters schema")
    print("[PASS] command argument")
    print("[PASS] cwd argument")
    print("[PASS] timeout argument")
    print("[PASS] Required command")

    print("\nSHELL TOOL SCHEMA TEST PASSED")


if __name__ == "__main__":
    main()
