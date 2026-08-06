from modules.planner import Planner

# ============================================================
# AI Assistant - Planner Test Suite
# Phase 4.5
# ============================================================

planner = Planner()

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
print("           AI Assistant - Planner Test")
print("=" * 60)

# ============================================================
# Test Data
# ============================================================

contexts = {

    "profile_name": {
        "intent": "profile_name",
        "message": "What is my name?",
        "entities": []
    },

    "profile_city": {
        "intent": "profile_city",
        "message": "Where do I live?",
        "entities": []
    },

    "preference": {
        "intent": "preference",
        "message": "What is my theme?",
        "entities": []
    },

    "task": {
        "intent": "task",
        "message": "Show my tasks",
        "entities": []
    },

    "conversation": {
        "intent": "conversation",
        "message": "Show conversation",
        "entities": []
    },

    "history": {
        "intent": "history",
        "message": "Show history",
        "entities": []
    },

    "general": {
        "intent": "general",
        "message": "Hello",
        "entities": []
    },

    "delete_files": {
        "intent": "delete_files",
        "message": "Delete screenshots",
        "entities": ["screenshots"]
    },

    "copy_file": {
        "intent": "copy_file",
        "message": "Copy report.pdf",
        "entities": ["report.pdf"]
    },

    "shutdown_system": {
        "intent": "shutdown_system",
        "message": "Shutdown laptop",
        "entities": []
    }

}

# ============================================================
# Test 1 : Profile Name
# ============================================================

print("\n--------------------------------------------")
print("Test 1 : Profile Name")
print("--------------------------------------------")

plan = planner.create_plan(contexts["profile_name"])

check("Intent",
      plan["intent"] == "profile_name")

check("Module",
      plan["module"] == "memory")

check("Action",
      plan["action"] == "get_profile")

# ============================================================
# Test 2 : Profile City
# ============================================================

print("\n--------------------------------------------")
print("Test 2 : Profile City")
print("--------------------------------------------")

plan = planner.create_plan(contexts["profile_city"])

check("Intent",
      plan["intent"] == "profile_city")

check("Module",
      plan["module"] == "memory")

check("Action",
      plan["action"] == "get_profile")

# ============================================================
# Test 3 : Preference
# ============================================================

print("\n--------------------------------------------")
print("Test 3 : Preference")
print("--------------------------------------------")

plan = planner.create_plan(contexts["preference"])

check("Intent",
      plan["intent"] == "preference")

check("Module",
      plan["module"] == "memory")

check("Action",
      plan["action"] == "get_preference")

# ============================================================
# Test 4 : Task
# ============================================================

print("\n--------------------------------------------")
print("Test 4 : Task")
print("--------------------------------------------")

plan = planner.create_plan(contexts["task"])

check("Intent",
      plan["intent"] == "task")

check("Module",
      plan["module"] == "memory")

check("Action",
      plan["action"] == "get_tasks")
# ============================================================
# Test 5 : Conversation
# ============================================================

print("\n--------------------------------------------")
print("Test 5 : Conversation")
print("--------------------------------------------")

plan = planner.create_plan(contexts["conversation"])

check("Intent",
      plan["intent"] == "conversation")

check("Module",
      plan["module"] == "memory")

check("Action",
      plan["action"] == "get_conversation")


# ============================================================
# Test 6 : History
# ============================================================

print("\n--------------------------------------------")
print("Test 6 : History")
print("--------------------------------------------")

plan = planner.create_plan(contexts["history"])

check("Intent",
      plan["intent"] == "history")

check("Module",
      plan["module"] == "memory")

check("Action",
      plan["action"] == "get_history")


# ============================================================
# Test 7 : General
# ============================================================

print("\n--------------------------------------------")
print("Test 7 : General")
print("--------------------------------------------")

plan = planner.create_plan(contexts["general"])

check("Intent",
      plan["intent"] == "general")

check("Module",
      plan["module"] == "chat")

check("Action",
      plan["action"] == "respond")


# ============================================================
# Test 8 : Delete Files
# ============================================================

print("\n--------------------------------------------")
print("Test 8 : Delete Files")
print("--------------------------------------------")

plan = planner.create_plan(contexts["delete_files"])

check("Intent",
      plan["intent"] == "delete_files")

check("Module",
      plan["module"] == "file_manager")

check("Action",
      plan["action"] == "delete")

check("High Risk",
      plan["risk"] == "high")

check("Confirmation Required",
      plan["confirmation"] is True)


# ============================================================
# Test 9 : Copy File
# ============================================================

print("\n--------------------------------------------")
print("Test 9 : Copy File")
print("--------------------------------------------")

plan = planner.create_plan(contexts["copy_file"])

check("Intent",
      plan["intent"] == "copy_file")

check("Module",
      plan["module"] == "file_manager")

check("Action",
      plan["action"] == "copy")

check("Parameters Exist",
      "entities" in plan["parameters"])


# ============================================================
# Test 10 : Shutdown System
# ============================================================

print("\n--------------------------------------------")
print("Test 10 : Shutdown System")
print("--------------------------------------------")

plan = planner.create_plan(contexts["shutdown_system"])

check("Intent",
      plan["intent"] == "shutdown_system")

check("Module",
      plan["module"] == "system")

check("Action",
      plan["action"] == "shutdown")

check("Risk",
      plan["risk"] == "high")

check("Confirmation",
      plan["confirmation"] is True)
# ============================================================
# Test 11 : Priority
# ============================================================

print("\n--------------------------------------------")
print("Test 11 : Priority")
print("--------------------------------------------")

plan = planner.create_plan(contexts["delete_files"])

check("Priority Exists",
      "priority" in plan)

check("High Priority",
      plan["priority"] == "high")

plan = planner.create_plan(contexts["general"])

check("Low Priority",
      plan["priority"] == "low")


# ============================================================
# Test 12 : Execution Steps
# ============================================================

print("\n--------------------------------------------")
print("Test 12 : Execution Steps")
print("--------------------------------------------")

plan = planner.create_plan(contexts["task"])

check("Steps Exist",
      "steps" in plan)

check("Steps are List",
      isinstance(plan["steps"], list))

check("Steps Available",
      len(plan["steps"]) > 0)


plan = planner.create_plan(contexts["delete_files"])

check("Delete Steps",
      len(plan["steps"]) == 3)


# ============================================================
# Test 13 : Estimated Time
# ============================================================

print("\n--------------------------------------------")
print("Test 13 : Estimated Time")
print("--------------------------------------------")

plan = planner.create_plan(contexts["general"])

check("Estimated Time Exists",
      "estimated_time" in plan)

check("Estimated Time Type",
      isinstance(plan["estimated_time"], int))

check("Estimated Time Positive",
      plan["estimated_time"] > 0)


plan = planner.create_plan(contexts["shutdown_system"])

check("Shutdown Time",
      plan["estimated_time"] == 5)


# ============================================================
# Test 14 : Parameters
# ============================================================

print("\n--------------------------------------------")
print("Test 14 : Parameters")
print("--------------------------------------------")

plan = planner.create_plan(contexts["copy_file"])

check("Parameters Dict",
      isinstance(plan["parameters"], dict))

check("Entities Present",
      "entities" in plan["parameters"])

check("Message Present",
      "message" in plan["parameters"])


# ============================================================
# Test 15 : Status
# ============================================================

print("\n--------------------------------------------")
print("Test 15 : Status")
print("--------------------------------------------")

plan = planner.create_plan(contexts["general"])

check("Status Exists",
      "status" in plan)

check("Status Ready",
      plan["status"] == "ready")

# ============================================================
# Test 16 : Unknown Intent
# ============================================================

print("\n--------------------------------------------")
print("Test 16 : Unknown Intent")
print("--------------------------------------------")

unknown_context = {
    "intent": "unknown_intent",
    "message": "Do something",
    "entities": []
}

plan = planner.create_plan(unknown_context)

check(
    "Fallback Module",
    plan["module"] == "chat"
)

check(
    "Fallback Action",
    plan["action"] == "respond"
)

check(
    "Fallback Risk",
    plan["risk"] == "low"
)

# ============================================================
# Test 17 : Complete Plan Validation
# ============================================================

print("\n--------------------------------------------")
print("Test 17 : Complete Plan Validation")
print("--------------------------------------------")

plan = planner.create_plan(contexts["task"])

required_keys = [

    "intent",
    "module",
    "action",
    "parameters",
    "risk",
    "confirmation",
    "priority",
    "steps",
    "estimated_time",
    "status"

]

for key in required_keys:

    check(
        f"{key} Exists",
        key in plan
    )

# ============================================================
# Test 18 : Data Types
# ============================================================

print("\n--------------------------------------------")
print("Test 18 : Data Types")
print("--------------------------------------------")

check(
    "Intent Type",
    isinstance(plan["intent"], str)
)

check(
    "Module Type",
    isinstance(plan["module"], str)
)

check(
    "Action Type",
    isinstance(plan["action"], str)
)

check(
    "Parameters Type",
    isinstance(plan["parameters"], dict)
)

check(
    "Risk Type",
    isinstance(plan["risk"], str)
)

check(
    "Confirmation Type",
    isinstance(plan["confirmation"], bool)
)

check(
    "Priority Type",
    isinstance(plan["priority"], str)
)

check(
    "Steps Type",
    isinstance(plan["steps"], list)
)

check(
    "Estimated Time Type",
    isinstance(plan["estimated_time"], int)
)

check(
    "Status Type",
    isinstance(plan["status"], str)
)

# ============================================================
# Summary
# ============================================================

print("\n" + "=" * 60)
print("            PLANNER TEST SUMMARY")
print("=" * 60)

print(f"\n✅ Passed : {passed}")
print(f"❌ Failed : {failed}")
print(f"📊 Total  : {passed + failed}")

if failed == 0:
    print("\n🎉 ALL TESTS PASSED")
    print("✅ Phase 4.5 Planner VERIFIED")
else:
    print("\n⚠️ Some tests failed.")
    print("Please fix the failed tests before continuing.")

print("\n" + "=" * 60)
