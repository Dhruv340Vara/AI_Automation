from modules.context import ContextEngine
from modules.memory import Memory

context = ContextEngine()
memory = Memory()
passed = 0
failed = 0

def test(name, condition):
    global passed, failed
    if condition:
        print(f"✅ PASS : {name}")
        passed += 1
    else:
        print(f"❌ FAIL : {name}")
        failed += 1

print("=" * 60)
print("        AI Assistant - Context Engine Test")
print("=" * 60)
print("\nPreparing Test Data...")
memory.clear()
memory.set_profile("name", "Dhruv")
memory.set_profile("city", "Rajkot")
memory.set_preference("theme", "dark")
memory.add_task({
    "title": "Complete Phase 4.4",
    "status": "pending"
})
memory.add_history("System Started")
memory.add_conversation(
    "assistant",
    "Hello Dhruv"
)
print("Done.\n")

print("--------------------------------------------")
print("Test 1 : Name")
print("--------------------------------------------")
result = context.get_context(
    "What is my name?"
)
test(
    "Intent",
    result["intent"] == "profile_name"
)
test(
    "Name Found",
    result["memory"]["name"]["success"] is True
)
test(
    "Correct Name",
    result["memory"]["name"]["value"] == "Dhruv"
)

print("\n--------------------------------------------")
print("Test 2 : City")
print("--------------------------------------------")
result = context.get_context(
    "What is my city?"
)
test(
    "City Intent",
    result["intent"] == "profile_city"
)
test(
    "City Found",
    result["memory"]["city"]["success"] is True
)
test(
    "Correct City",
    result["memory"]["city"]["value"] == "Rajkot"
)

print("\n--------------------------------------------")
print("Test 3 : Theme")
print("--------------------------------------------")
result = context.get_context(
    "Use dark theme"
)
test(
    "Preference Intent",
    result["intent"] == "preference"
)
test(
    "Theme Found",
    result["memory"]["theme"]["success"] is True
)
test(
    "Correct Theme",
    result["memory"]["theme"]["value"] == "dark"
)

print("\n--------------------------------------------")
print("Test 4 : Tasks")
print("--------------------------------------------")
result = context.get_context(
    "Show my tasks"
)
test(
    "Task Intent",
    result["intent"] == "task"
)
test(
    "Task List",
    isinstance(result["memory"]["tasks"], list)
)
test(
    "Task Count",
    len(result["memory"]["tasks"]) >= 1
)
test(
    "Task Title",
    result["memory"]["tasks"][-1]["title"] == "Complete Phase 4.4"
)

print("\n--------------------------------------------")
print("Test 5 : Conversation")
print("--------------------------------------------")
conversation = result["memory"]["conversation"]
test(
    "Conversation is List",
    isinstance(conversation, list)
)
test(
    "Conversation Available",
    len(conversation) >= 1
)
last = conversation[-1]
test(
    "Conversation Role Exists",
    "role" in last
)
test(
    "Conversation Message Exists",
    "message" in last
)

print("\n--------------------------------------------")
print("Test 6 : History")
print("--------------------------------------------")
history = result["memory"]["history"]
test(
    "History is List",
    isinstance(history, list)
)
test(
    "History Available",
    len(history) >= 1
)
last = history[-1]
test(
    "History Action Exists",
    "action" in last
)
test(
    "History Time Exists",
    "time" in last
)

print("\n--------------------------------------------")
print("Test 7 : Entity Extraction")
print("--------------------------------------------")
entities = context.extract_entities(
    "My name is Dhruv and city is Rajkot"
)
test(
    "Entity List",
    isinstance(entities, list)
)
test(
    "Contains Name",
    "Dhruv" in entities
)
test(
    "Contains City",
    "Rajkot" in entities
)

print("\n--------------------------------------------")
print("Test 8 : Gujarati Name")
print("--------------------------------------------")
result = context.get_context(
    "મારું નામ શું છે?"
)
test(
    "Gujarati Name Intent",
    result["intent"] == "profile_name"
)
test(
    "Gujarati Name Found",
    result["memory"]["name"]["success"] is True
)
test(
    "Gujarati Correct Name",
    result["memory"]["name"]["value"] == "Dhruv"
)

print("\n--------------------------------------------")
print("Test 9 : Unknown Query")
print("--------------------------------------------")
result = context.get_context(
    "Today's weather"
)
test(
    "General Intent",
    result["intent"] == "general"
)

print("\n--------------------------------------------")
print("Test 10 : Auto Conversation Save")
print("--------------------------------------------")
conversation = memory.get_conversation()
test(
    "Conversation Saved",
    len(conversation) >= 5
)
test(
    "Last Role is User",
    conversation[-1]["role"] == "user"
)

print("\n--------------------------------------------")
print("Test 11 : Auto History Save")
print("--------------------------------------------")
history = memory.get_history()
test(
    "History Saved",
    len(history) >= 5
)
test(
    "Last Action Exists",
    "Context generated for:" in history[-1]["action"]
)

print("\n--------------------------------------------")
print("Test 12 : Context Structure")
print("--------------------------------------------")
required_keys = [
    "message",
    "intent",
    "entities",
    "memory"
]
test(
    "Context is Dictionary",
    isinstance(result, dict)
)
test(
    "Required Keys Present",
    all(key in result for key in required_keys)
)

print("\n" + "=" * 60)
print("           CONTEXT ENGINE TEST SUMMARY")
print("=" * 60)
print(f"\n✅ Passed : {passed}")
print(f"❌ Failed : {failed}")
total = passed + failed
print(f"📊 Total : {total}")
if failed == 0:
    print("\n🎉 ALL TESTS PASSED")
    print("✅ Phase 4.4 Context Engine VERIFIED")
else:
    print("\n⚠ Some tests failed.")
    print("Please fix the failed tests before Phase 4.5")
print("\n" + "=" * 60)
