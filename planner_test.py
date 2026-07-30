from modules.planner import Planner

planner = Planner()

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
print("          AI Planner Test")
print("=" * 60)


# =====================================================
# Test 1 : Profile Name
# =====================================================

context = {
    "message": "What is my name?",
    "intent": "profile_name",
    "entities": ["What", "name"]
}

plan = planner.create_plan(context)

test("Profile Module", plan["module"] == "memory")
test("Profile Action", plan["action"] == "get_profile")
test("Low Risk", plan["risk"] == "low")
test("No Confirmation", plan["confirmation"] is False)


# =====================================================
# Test 2 : Profile City
# =====================================================

context = {
    "message": "What is my city?",
    "intent": "profile_city",
    "entities": ["city"]
}

plan = planner.create_plan(context)

test("City Module", plan["module"] == "memory")
test("City Action", plan["action"] == "get_profile")


# =====================================================
# Test 3 : Preference
# =====================================================

context = {
    "message": "Use dark theme",
    "intent": "preference",
    "entities": ["dark", "theme"]
}

plan = planner.create_plan(context)

test("Preference Module", plan["module"] == "memory")
test("Preference Action", plan["action"] == "get_preference")


# =====================================================
# Test 4 : Tasks
# =====================================================

context = {
    "message": "Show my tasks",
    "intent": "task",
    "entities": ["tasks"]
}

plan = planner.create_plan(context)

test("Task Module", plan["module"] == "memory")
test("Task Action", plan["action"] == "get_tasks")


# =====================================================
# Test 5 : General Chat
# =====================================================

context = {
    "message": "Hello",
    "intent": "general",
    "entities": []
}

plan = planner.create_plan(context)

test("Chat Module", plan["module"] == "chat")
test("Chat Action", plan["action"] == "respond")


# =====================================================
# Test 6 : Parameters
# =====================================================

context = {
    "message": "My name",
    "intent": "profile_name",
    "entities": ["My", "name"]
}

plan = planner.create_plan(context)

test("Message Parameter",
     plan["parameters"]["message"] == "My name")

test("Entities Parameter",
     isinstance(plan["parameters"]["entities"], list))


# =====================================================
# Test 7 : Risk Analysis
# =====================================================

test(
    "High Risk",
    planner.analyze_risk("delete_files") == "high"
)

test(
    "Medium Risk",
    planner.analyze_risk("move_file") == "medium"
)

test(
    "Low Risk",
    planner.analyze_risk("profile_name") == "low"
)


# =====================================================
# Test 8 : Confirmation
# =====================================================

test(
    "High Confirmation",
    planner.needs_confirmation("high") is True
)

test(
    "Medium Confirmation",
    planner.needs_confirmation("medium") is True
)

test(
    "Low Confirmation",
    planner.needs_confirmation("low") is False
)


# =====================================================
# Test 9 : Unknown Intent
# =====================================================

context = {
    "message": "Random Text",
    "intent": "unknown",
    "entities": []
}

plan = planner.create_plan(context)

test(
    "Unknown -> Chat",
    plan["module"] == "chat"
)


# =====================================================
# Test 10 : Plan Structure
# =====================================================

required = [
    "intent",
    "module",
    "action",
    "parameters",
    "confirmation",
    "risk",
    "status"
]

test(
    "Plan Dictionary",
    isinstance(plan, dict)
)

test(
    "Required Keys",
    all(key in plan for key in required)
)


# =====================================================
# Test 11 : Status
# =====================================================

test(
    "Status Ready",
    plan["status"] == "ready"
)


# =====================================================
# Summary
# =====================================================

print("\n" + "=" * 60)
print("           PLANNER TEST SUMMARY")
print("=" * 60)

print(f"\n✅ Passed : {passed}")
print(f"❌ Failed : {failed}")

total = passed + failed
print(f"📊 Total : {total}")

if failed == 0:
    print("\n🎉 ALL TESTS PASSED")
    print("✅ Phase 4.5 Planner VERIFIED")
else:
    print("\n⚠ Some tests failed.")
    print("Please fix the failed tests.")

print("\n" + "=" * 60)
