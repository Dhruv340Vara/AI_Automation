from automation.ai.tool_call import ToolCall


print("=== Tool Call Format Test ===")


# 1. Create ToolCall
call = ToolCall(
    tool="Shell",
    arguments={
        "command": "pwd"
    },
)

print("\n1. ToolCall created")
print(call)

assert call.tool == "Shell"
assert call.arguments["command"] == "pwd"
assert call.is_valid()

print("[PASS] ToolCall created correctly")


# 2. Convert to dictionary
data = call.to_dict()

print("\n2. ToolCall dictionary")
print(data)

assert data["type"] == "tool_call"
assert data["tool"] == "Shell"
assert data["arguments"]["command"] == "pwd"
assert data["id"]

print("[PASS] to_dict() works")


# 3. Restore from dictionary
restored = ToolCall.from_dict(data)

print("\n3. ToolCall restored")
print(restored)

assert restored.tool == call.tool
assert restored.arguments == call.arguments
assert restored.call_id == call.call_id

print("[PASS] from_dict() works")


# 4. Invalid type
try:
    ToolCall.from_dict({
        "type": "final_answer",
        "tool": "Shell",
        "arguments": {},
    })

    raise AssertionError(
        "Invalid type was accepted"
    )

except ValueError:
    print(
        "[PASS] Invalid tool call rejected"
    )


# 5. Invalid arguments
try:
    ToolCall(
        tool="Shell",
        arguments="pwd",
    )

    raise AssertionError(
        "Invalid arguments were accepted"
    )

except TypeError:
    print(
        "[PASS] Invalid arguments rejected"
    )


print(
    "\nTOOL CALL FORMAT TEST PASSED"
)
