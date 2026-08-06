from modules.brain import Brain
brain = Brain()

passed = 0
failed = 0


def check(name, condition):
    global passed, failed

    if condition:
        print(f"[PASS] {name}")
        passed += 1
    else:
        print(f"[FAIL] {name}")
        failed += 1


print("=" * 60)
print("          BRAIN TEST SUITE")
print("=" * 60)

# ============================================================
# Test 1 : Initialization
# ============================================================

print("\n--------------------------------------------")
print("Test 1 : Initialization")
print("--------------------------------------------")

check(
    "Brain Instance",
    isinstance(brain, Brain)
)

check(
    "Parser Exists",
    hasattr(brain, "parser")
)

check(
    "Context Exists",
    hasattr(brain, "context")
)

check(
    "Planner Exists",
    hasattr(brain, "planner")
)

check(
    "Executor Exists",
    hasattr(brain, "executor")
)

# ============================================================
# Test 2 : Status
# ============================================================

print("\n--------------------------------------------")
print("Test 2 : Status")
print("--------------------------------------------")

status = brain.status()

check(
    "Status Dictionary",
    isinstance(status, dict)
)

check(
    "Pipeline Ready",
    status.get("pipeline") == "ready"
)

check(
    "Parser Ready",
    status.get("parser") is True
)

check(
    "Context Ready",
    status.get("context") is True
)

check(
    "Planner Ready",
    status.get("planner") is True
)

check(
    "Executor Ready",
    status.get("executor") is True
)

# ============================================================
# Test 3 : Pipeline
# ============================================================

print("\n--------------------------------------------")
print("Test 3 : Pipeline")
print("--------------------------------------------")

pipeline = brain.pipeline()

check(
    "Pipeline List",
    isinstance(pipeline, list)
)

check(
    "Pipeline Length",
    len(pipeline) == 4
)

expected = [
    "Parser",
    "Context",
    "Planner",
    "Executor"
]

for item in expected:
    check(
        f"{item} Present",
        item in pipeline
    )

# ============================================================
# Test 4 : Process
# ============================================================

print("\n--------------------------------------------")
print("Test 4 : Process")
print("--------------------------------------------")

response = brain.process("What is my name?")

check(
    "Process Returns Dictionary",
    isinstance(response, dict)
)

check(
    "Success Key Exists",
    "success" in response
)

check(
    "Message Key Exists",
    "message" in response
)

check(
    "Context Key Exists",
    "context" in response
)

check(
    "Plan Key Exists",
    "plan" in response
)

check(
    "Result Key Exists",
    "result" in response
)

check(
    "Execution Time Exists",
    "execution_time" in response
)

# ============================================================
# Test 5 : Data Types
# ============================================================

print("\n--------------------------------------------")
print("Test 5 : Data Types")
print("--------------------------------------------")

check(
    "Success Type",
    isinstance(response["success"], bool)
)

check(
    "Message Type",
    isinstance(response["message"], str)
)

check(
    "Context Type",
    isinstance(response["context"], dict)
)

check(
    "Plan Type",
    isinstance(response["plan"], dict)
)

check(
    "Result Type",
    isinstance(response["result"], dict)
)

check(
    "Execution Time Type",
    isinstance(
        response["execution_time"],
        (int, float)
    )
)

# ============================================================
# Test 6 : Statistics
# ============================================================

print("\n--------------------------------------------")
print("Test 6 : Statistics")
print("--------------------------------------------")

stats = brain.statistics()

check(
    "Statistics Dictionary",
    isinstance(stats, dict)
)

required = [
    "total_requests",
    "successful_requests",
    "failed_requests",
    "success_rate"
]

for key in required:

    check(
        f"{key} Exists",
        key in stats
    )

check(
    "Total Requests >= 1",
    stats["total_requests"] >= 1
)

check(
    "Successful Requests >= 0",
    stats["successful_requests"] >= 0
)

check(
    "Failed Requests >= 0",
    stats["failed_requests"] >= 0
)

check(
    "Success Rate Numeric",
    isinstance(
        stats["success_rate"],
        (int, float)
    )
)

# ============================================================
# Test 7 : Multiple Requests
# ============================================================

print("\n--------------------------------------------")
print("Test 7 : Multiple Requests")
print("--------------------------------------------")

messages = [

    "Hello",

    "What is my city?",

    "Show my tasks"

]

for i, msg in enumerate(messages, start=1):

    result = brain.process(msg)

    check(
        f"Request {i}",
        isinstance(result, dict)
    )

    check(
        f"Request {i} Success Key",
        "success" in result
    )
# ============================================================
# Test 8 : Reset Statistics
# ============================================================

print("\n--------------------------------------------")
print("Test 8 : Reset Statistics")
print("--------------------------------------------")

brain.reset_statistics()

stats = brain.statistics()

check(
    "Total Requests Reset",
    stats["total_requests"] == 0
)

check(
    "Successful Requests Reset",
    stats["successful_requests"] == 0
)

check(
    "Failed Requests Reset",
    stats["failed_requests"] == 0
)

check(
    "Success Rate Reset",
    stats["success_rate"] == 0
)

# ============================================================
# Test 9 : Invalid Input
# ============================================================

print("\n--------------------------------------------")
print("Test 9 : Invalid Input")
print("--------------------------------------------")

invalid_inputs = [
    "",
    None,
    123,
    [],
    {}
]

for i, value in enumerate(invalid_inputs, start=1):

    try:

        result = brain.process(value)

        check(
            f"Invalid Input {i}",
            isinstance(result, dict)
        )

        check(
            f"Invalid Input {i} Success Key",
            "success" in result
        )

    except Exception:

        check(
            f"Invalid Input {i}",
            False
        )

# ============================================================
# Test 10 : Consecutive Executions
# ============================================================

print("\n--------------------------------------------")
print("Test 10 : Consecutive Executions")
print("--------------------------------------------")

for i in range(10):

    result = brain.process("Hello")

    check(
        f"Execution {i+1}",
        isinstance(result, dict)
    )

# ============================================================
# Test 11 : Pipeline Consistency
# ============================================================

print("\n--------------------------------------------")
print("Test 11 : Pipeline Consistency")
print("--------------------------------------------")

pipeline = brain.pipeline()

check(
    "Pipeline Still List",
    isinstance(pipeline, list)
)

check(
    "Pipeline Size",
    len(pipeline) == 4
)

expected_pipeline = [
    "Parser",
    "Context",
    "Planner",
    "Executor"
]

for module in expected_pipeline:

    check(
        f"{module} Available",
        module in pipeline
    )

# ============================================================
# Test 12 : Status After Executions
# ============================================================

print("\n--------------------------------------------")
print("Test 12 : Status After Executions")
print("--------------------------------------------")

status = brain.status()

check(
    "Status Dictionary",
    isinstance(status, dict)
)

check(
    "Pipeline Ready",
    status["pipeline"] == "ready"
)

check(
    "Parser Active",
    status["parser"] is True
)

check(
    "Context Active",
    status["context"] is True
)

check(
    "Planner Active",
    status["planner"] is True
)

check(
    "Executor Active",
    status["executor"] is True
)

# ============================================================
# Test 13 : Statistics Growth
# ============================================================

print("\n--------------------------------------------")
print("Test 13 : Statistics Growth")
print("--------------------------------------------")

stats = brain.statistics()

check(
    "Total Requests Increased",
    stats["total_requests"] >= 10
)

check(
    "Success Rate Valid",
    0 <= stats["success_rate"] <= 100
)

# ============================================================
# Test 14 : Brain Components
# ============================================================

print("\n--------------------------------------------")
print("Test 14 : Brain Components")
print("--------------------------------------------")

components = [
    ("parser", brain.parser),
    ("context", brain.context),
    ("planner", brain.planner),
    ("executor", brain.executor)
]

for name, component in components:

    check(
        f"{name.capitalize()} Exists",
        component is not None
    )

# ============================================================
# Test 15 : Process Stability
# ============================================================

print("\n--------------------------------------------")
print("Test 15 : Process Stability")
print("--------------------------------------------")

test_messages = [
    "Hello",
    "What is my name?",
    "What is my city?",
    "Show my tasks",
    "Open calculator"
]

for index, message in enumerate(test_messages, start=1):

    try:

        result = brain.process(message)

        check(
            f"Stable Request {index}",
            isinstance(result, dict)
        )

        check(
            f"Stable Request {index} Success",
            "success" in result
        )

    except Exception:

        check(
            f"Stable Request {index}",
            False
        )

# ============================================================
# Test 16 : Statistics Consistency
# ============================================================

print("\n--------------------------------------------")
print("Test 16 : Statistics Consistency")
print("--------------------------------------------")

stats = brain.statistics()

check(
    "Statistics Type",
    isinstance(stats, dict)
)

check(
    "Total >= Success",
    stats["total_requests"] >= stats["successful_requests"]
)

check(
    "Total >= Failed",
    stats["total_requests"] >= stats["failed_requests"]
)

check(
    "Request Count Consistent",
    stats["successful_requests"] + stats["failed_requests"] <= stats["total_requests"]
)

# ============================================================
# Test 17 : Public API
# ============================================================

print("\n--------------------------------------------")
print("Test 17 : Public API")
print("--------------------------------------------")

public_methods = [
    "process",
    "status",
    "statistics",
    "pipeline",
    "reset_statistics"
]

for method in public_methods:

    check(
        f"{method}() Available",
        hasattr(brain, method)
    )

# ============================================================
# Final Summary
# ============================================================

print("\n" + "=" * 60)
print("              BRAIN TEST SUMMARY")
print("=" * 60)

print(f"\n✅ Passed : {passed}")
print(f"❌ Failed : {failed}")
print(f"📊 Total  : {passed + failed}")

if failed == 0:

    print("\n🎉 ALL TESTS PASSED")
    print("✅ Phase 4.7 Brain VERIFIED")

else:

    print("\n⚠ Some tests failed.")
    print("Please fix the failed tests before continuing.")

print("\n" + "=" * 60)
