from modules.executor import Executor

executor = Executor()
passed = 0
failed = 0

def check(title, condition):
    global passed, failed

    if condition:
        print(f"✅ PASS : {title}")
        passed += 1
    else:
        print(f"❌ FAIL : {title}")
        failed += 1


print("=" * 60)
print("           AI Assistant - Executor Test")
print("=" * 60)

# ============================================================
# Test Data
# ============================================================

memory_plan = {
    "module": "memory",
    "action": "get_tasks",
    "parameters": {
        "message": "Show my tasks",
        "entities": []
    }
}

chat_plan = {
    "module": "chat",
    "action": "respond",
    "parameters": {
        "message": "Hello"
    }
}

unknown_plan = {
    "module": "unknown",
    "action": "nothing",
    "parameters": {}
}

# ============================================================
# Test 1 : Module Registry
# ============================================================

print("\n--------------------------------------------")
print("Test 1 : Module Registry")
print("--------------------------------------------")

check(
    "Registry Exists",
    hasattr(executor, "module_handlers")
)

check(
    "Registry Type",
    isinstance(executor.module_handlers, dict)
)

expected_modules = [
    "memory",
    "chat",
    "file_manager",
    "app_manager",
    "system"
]

for module in expected_modules:

    check(
        f"{module} Registered",
        module in executor.module_handlers
    )

# ============================================================
# Test 2 : Memory Registry
# ============================================================

print("\n--------------------------------------------")
print("Test 2 : Memory Registry")
print("--------------------------------------------")

check(
    "Memory Registry Exists",
    hasattr(executor, "memory_handlers")
)

check(
    "Memory Registry Type",
    isinstance(executor.memory_handlers, dict)
)

expected_actions = [
    "get_profile",
    "get_preference",
    "get_tasks",
    "get_conversation",
    "get_history"
]

for action in expected_actions:

    check(
        f"{action} Registered",
        action in executor.memory_handlers
    )

# ============================================================
# Test 3 : Available Modules
# ============================================================

print("\n--------------------------------------------")
print("Test 3 : Available Modules")
print("--------------------------------------------")

modules = executor.available_modules()

check(
    "Returns List",
    isinstance(modules, list)
)

check(
    "Memory Present",
    "memory" in modules
)

check(
    "Chat Present",
    "chat" in modules
)

check(
    "System Present",
    "system" in modules
)
# ============================================================
# Test 4 : Memory Execution
# ============================================================

print("\n--------------------------------------------")
print("Test 4 : Memory Execution")
print("--------------------------------------------")

result = executor.execute(memory_plan)

check(
    "Result is Dictionary",
    isinstance(result, dict)
)

check(
    "Success Key Exists",
    "success" in result
)

check(
    "Success Type",
    isinstance(result["success"], bool)
)

check(
    "Data Or Message Exists",
    ("data" in result) or ("message" in result)
)

# ============================================================
# Test 5 : Chat Execution
# ============================================================

print("\n--------------------------------------------")
print("Test 5 : Chat Execution")
print("--------------------------------------------")

result = executor.execute(chat_plan)

check(
    "Chat Result is Dictionary",
    isinstance(result, dict)
)

check(
    "Chat Success",
    result.get("success") is True
)

check(
    "Message Exists",
    "message" in result
)

check(
    "Message Type",
    isinstance(result["message"], str)
)

# ============================================================
# Test 6 : Unknown Module
# ============================================================

print("\n--------------------------------------------")
print("Test 6 : Unknown Module")
print("--------------------------------------------")

result = executor.execute(unknown_plan)

check(
    "Unknown Result Dict",
    isinstance(result, dict)
)

check(
    "Unknown Success False",
    result.get("success") is False
)

check(
    "Unknown Message Exists",
    "message" in result
)

# ============================================================
# Test 7 : Module Support
# ============================================================

print("\n--------------------------------------------")
print("Test 7 : Module Support")
print("--------------------------------------------")

check(
    "Memory Supported",
    executor.is_module_supported("memory")
)

check(
    "Chat Supported",
    executor.is_module_supported("chat")
)

check(
    "File Manager Supported",
    executor.is_module_supported("file_manager")
)

check(
    "App Manager Supported",
    executor.is_module_supported("app_manager")
)

check(
    "System Supported",
    executor.is_module_supported("system")
)

check(
    "Unknown Not Supported",
    not executor.is_module_supported("unknown")
)

# ============================================================
# Test 8 : Execute Return Structure
# ============================================================

print("\n--------------------------------------------")
print("Test 8 : Execute Return Structure")
print("--------------------------------------------")

result = executor.execute(chat_plan)

required = [
    "success",
    "message"
]

for key in required:

    check(
        f"{key} Exists",
        key in result
    )
# ============================================================
# Test 9 : Statistics
# ============================================================

print("\n--------------------------------------------")
print("Test 9 : Statistics")
print("--------------------------------------------")

stats = executor.statistics()

check(
    "Statistics Dictionary",
    isinstance(stats, dict)
)

check(
    "Modules Key",
    "modules" in stats
)

check(
    "Memory Actions Key",
    "memory_actions" in stats
)

check(
    "Supported Modules Key",
    "supported_modules" in stats
)

check(
    "Supported Modules Type",
    isinstance(stats["supported_modules"], list)
)

check(
    "Module Count",
    stats["modules"] >= 5
)

check(
    "Memory Action Count",
    stats["memory_actions"] >= 5
)

# ============================================================
# Test 10 : Memory Handlers
# ============================================================

print("\n--------------------------------------------")
print("Test 10 : Memory Handlers")
print("--------------------------------------------")

for action in executor.memory_handlers:

    check(
        f"{action} Callable",
        callable(executor.memory_handlers[action])
    )

# ============================================================
# Test 11 : Module Handlers
# ============================================================

print("\n--------------------------------------------")
print("Test 11 : Module Handlers")
print("--------------------------------------------")

for module in executor.module_handlers:

    check(
        f"{module} Callable",
        callable(executor.module_handlers[module])
    )

# ============================================================
# Test 12 : Multiple Execution
# ============================================================

print("\n--------------------------------------------")
print("Test 12 : Multiple Execution")
print("--------------------------------------------")

plans = [
    memory_plan,
    chat_plan,
    unknown_plan
]

for index, plan in enumerate(plans, start=1):

    result = executor.execute(plan)

    check(
        f"Execution {index}",
        isinstance(result, dict)
    )

# ============================================================
# Test 13 : Error Handling
# ============================================================

print("\n--------------------------------------------")
print("Test 13 : Error Handling")
print("--------------------------------------------")

bad_plan = {
    "module": None,
    "action": None
}

result = executor.execute(bad_plan)

check(
    "Bad Plan Returns Dict",
    isinstance(result, dict)
)

check(
    "Bad Plan Failed",
    result["success"] is False
)

check(
    "Bad Plan Message",
    "message" in result
)

# ============================================================
# Test 14 : Module Names
# ============================================================

print("\n--------------------------------------------")
print("Test 14 : Module Names")
print("--------------------------------------------")

modules = executor.available_modules()

expected = [
    "memory",
    "chat",
    "file_manager",
    "app_manager",
    "system"
]

for module in expected:

    check(
        f"{module} Available",
        module in modules
    )

# ============================================================
# Test 15 : Complete Validation
# ============================================================

print("\n--------------------------------------------")
print("Test 15 : Complete Validation")
print("--------------------------------------------")

result = executor.execute(chat_plan)

required_keys = [
    "success",
    "message"
]

for key in required_keys:

    check(
        f"{key} Exists",
        key in result
    )

# ============================================================
# Test 16 : Data Types
# ============================================================

print("\n--------------------------------------------")
print("Test 16 : Data Types")
print("--------------------------------------------")

check(
    "Success Type",
    isinstance(result["success"], bool)
)

check(
    "Message Type",
    isinstance(result["message"], str)
)

# ============================================================
# Test 17 : Memory Result Validation
# ============================================================

print("\n--------------------------------------------")
print("Test 17 : Memory Result")
print("--------------------------------------------")

result = executor.execute(memory_plan)

check(
    "Memory Result Dict",
    isinstance(result, dict)
)

check(
    "Memory Success Exists",
    "success" in result
)

check(
    "Memory Success Type",
    isinstance(result["success"], bool)
)

check(
    "Memory Contains Data Or Message",
    ("data" in result) or ("message" in result)
)

# ============================================================
# Test 18 : Registry Size
# ============================================================

print("\n--------------------------------------------")
print("Test 18 : Registry Size")
print("--------------------------------------------")

check(
    "Module Registry Size",
    len(executor.module_handlers) >= 5
)

check(
    "Memory Registry Size",
    len(executor.memory_handlers) >= 5
)

# ============================================================
# Summary
# ============================================================

print("\n" + "=" * 60)
print("            EXECUTOR TEST SUMMARY")
print("=" * 60)

print(f"\n✅ Passed : {passed}")
print(f"❌ Failed : {failed}")
print(f"📊 Total  : {passed + failed}")

if failed == 0:
    print("\n🎉 ALL TESTS PASSED")
    print("✅ Phase 4.6 Executor VERIFIED")
else:
    print("\n⚠️ Some tests failed.")
    print("Please fix the failed tests before continuing.")

print("\n" + "=" * 60)
