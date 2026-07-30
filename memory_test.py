from modules.memory import Memory

memory = Memory()

passed = 0
failed = 0


# =====================================================
# Helper Function
# =====================================================

def test(name, condition):
    global passed, failed

    if condition:
        print(f"✅ PASS : {name}")
        passed += 1
    else:
        print(f"❌ FAIL : {name}")
        failed += 1


# =====================================================
# Header
# =====================================================

print("=" * 60)
print("      AI Assistant - Phase 4.3 Memory Test")
print("=" * 60)

print("\nCleaning Memory...")

memory.clear()

print("Done.\n")


# =====================================================
# Test 1 : remember()
# =====================================================

print("--------------------------------------------------")
print("Test 1 : remember()")
print("--------------------------------------------------")

res = memory.remember("name", "Dhruv")

test(
    "remember() returns success",
    res.get("success") is True
)

res = memory.recall("name")

test(
    "remember() stored correct value",
    res.get("value") == "Dhruv"
)


# =====================================================
# Test 2 : Update Existing Key
# =====================================================

print("\n--------------------------------------------------")
print("Test 2 : Update Existing Key")
print("--------------------------------------------------")

memory.remember("name", "Dhruv Vara")

res = memory.recall("name")

test(
    "Updated value",
    res.get("value") == "Dhruv Vara"
)


# =====================================================
# Test 3 : Multiple Generic Values
# =====================================================

print("\n--------------------------------------------------")
print("Test 3 : Multiple Generic Values")
print("--------------------------------------------------")

memory.remember("city", "Rajkot")
memory.remember("college", "LDRP")

all_memory = memory.all()

test(
    "City saved",
    all_memory.get("city") == "Rajkot"
)

test(
    "College saved",
    all_memory.get("college") == "LDRP"
)


# =====================================================
# Test 4 : recall() Missing Key
# =====================================================

print("\n--------------------------------------------------")
print("Test 4 : Missing Key")
print("--------------------------------------------------")

res = memory.recall("unknown_key")

test(
    "Missing key returns False",
    res.get("success") is False
)


# =====================================================
# Test 5 : forget()
# =====================================================

print("\n--------------------------------------------------")
print("Test 5 : forget()")
print("--------------------------------------------------")

memory.forget("city")

all_memory = memory.all()

test(
    "City deleted",
    "city" not in all_memory
)


# =====================================================
# Test 6 : Delete Unknown Key
# =====================================================

print("\n--------------------------------------------------")
print("Test 6 : Delete Unknown Key")
print("--------------------------------------------------")

try:
    memory.forget("does_not_exist")

    test(
        "Deleting unknown key does not crash",
        True
    )

except Exception:

    test(
        "Deleting unknown key does not crash",
        False
    )
# =====================================================
# Test 7 : Profile
# =====================================================

print("\n--------------------------------------------------")
print("Test 7 : Profile")
print("--------------------------------------------------")

res = memory.set_profile("name", "Dhruv")

test(
    "set_profile() returns success",
    res.get("success") is True
)

res = memory.get_profile("name")

test(
    "Profile name saved",
    res.get("success") is True and
    res.get("value") == "Dhruv"
)

res = memory.get_profile("age")

test(
    "Missing profile returns False",
    res.get("success") is False
)


# =====================================================
# Test 8 : Preferences
# =====================================================

print("\n--------------------------------------------------")
print("Test 8 : Preferences")
print("--------------------------------------------------")

res = memory.set_preference("theme", "dark")

test(
    "set_preference() returns success",
    res.get("success") is True
)

res = memory.get_preference("theme")

test(
    "Preference saved",
    res.get("success") is True and
    res.get("value") == "dark"
)

res = memory.get_preference("language")

test(
    "Missing preference returns False",
    res.get("success") is False
)


# =====================================================
# Test 9 : Conversation
# =====================================================

print("\n--------------------------------------------------")
print("Test 9 : Conversation")
print("--------------------------------------------------")

res = memory.add_conversation(
    "user",
    "Hello AI"
)

test(
    "User conversation added",
    res.get("success") is True
)

res = memory.add_conversation(
    "assistant",
    "Hello Dhruv"
)

test(
    "Assistant conversation added",
    res.get("success") is True
)

conversation = memory.get_conversation()

test(
    "Conversation is list",
    isinstance(conversation, list)
)

test(
    "Conversation count >= 2",
    len(conversation) >= 2
)

last = conversation[-1]

test(
    "Last message role",
    last.get("role") == "assistant"
)

test(
    "Last message text",
    last.get("message") == "Hello Dhruv"
)

test(
    "Conversation contains timestamp",
    "time" in last
)
# =====================================================
# Test 10 : Tasks
# =====================================================

print("\n--------------------------------------------------")
print("Test 10 : Tasks")
print("--------------------------------------------------")

res = memory.add_task({
    "title": "Complete Phase 4.3",
    "status": "pending"
})

test(
    "Task added",
    res.get("success") is True
)

tasks = memory.get_tasks()

test(
    "Tasks is list",
    isinstance(tasks, list)
)

test(
    "Task count >= 1",
    len(tasks) >= 1
)

test(
    "Task title correct",
    tasks[-1].get("title") == "Complete Phase 4.3"
)


# =====================================================
# Test 11 : History
# =====================================================

print("\n--------------------------------------------------")
print("Test 11 : History")
print("--------------------------------------------------")

res = memory.add_history("Memory Test Started")

test(
    "History added",
    res.get("success") is True
)

history = memory.get_history()

test(
    "History is list",
    isinstance(history, list)
)

test(
    "History count >= 1",
    len(history) >= 1
)

test(
    "History action correct",
    history[-1].get("action") == "Memory Test Started"
)

test(
    "History contains timestamp",
    "time" in history[-1]
)


# =====================================================
# Test 12 : Unicode
# =====================================================

print("\n--------------------------------------------------")
print("Test 12 : Unicode")
print("--------------------------------------------------")

memory.remember("language", "ગુજરાતી")

res = memory.recall("language")

test(
    "Unicode stored correctly",
    res.get("success") is True and
    res.get("value") == "ગુજરાતી"
)


# =====================================================
# Test 13 : Large Text
# =====================================================

print("\n--------------------------------------------------")
print("Test 13 : Large Text")
print("--------------------------------------------------")

large_text = "Hello AI! " * 1000

memory.remember("large_text", large_text)

res = memory.recall("large_text")

test(
    "Large text stored correctly",
    res.get("success") is True and
    res.get("value") == large_text
)


# =====================================================
# Test 14 : all()
# =====================================================

print("\n--------------------------------------------------")
print("Test 14 : all()")
print("--------------------------------------------------")

all_data = memory.all()

required_keys = [
    "profile",
    "preferences",
    "conversation",
    "tasks",
    "history"
]

test(
    "all() returns dict",
    isinstance(all_data, dict)
)

test(
    "Required sections exist",
    all(key in all_data for key in required_keys)
)


# =====================================================
# Test 15 : clear()
# =====================================================

print("\n--------------------------------------------------")
print("Test 15 : clear()")
print("--------------------------------------------------")

res = memory.clear()

test(
    "clear() success",
    res.get("success") is True
)

all_data = memory.all()

test(
    "Profile cleared",
    all_data["profile"] == {}
)

test(
    "Preferences cleared",
    all_data["preferences"] == {}
)

test(
    "Conversation cleared",
    all_data["conversation"] == []
)

test(
    "Tasks cleared",
    all_data["tasks"] == []
)

test(
    "History cleared",
    all_data["history"] == []
)


# =====================================================
# Final Summary
# =====================================================

print("\n" + "=" * 60)
print("              TEST SUMMARY")
print("=" * 60)

print(f"\n✅ Passed : {passed}")
print(f"❌ Failed : {failed}")

total = passed + failed

print(f"📊 Total  : {total}")

if failed == 0:
    print("\n🎉 ALL TESTS PASSED")
    print("✅ Phase 4.3 Memory System is VERIFIED.")
else:
    print("\n⚠ Some tests failed.")
    print("Please review the failed tests before moving to Phase 4.4.")

print("\n" + "=" * 60)
