from __future__ import annotations

print("=" * 60)
print("          PLANNER TEST SUITE")
print("=" * 60)

from automation.ai.intent import (
    Intent,
)

from automation.ai.intent_types import (
    IntentType,
)

from automation.ai.planner import (
    Planner,
)

from automation.ai.plan_executor import (
    PlanExecutor,
)

# ==================================================
# Planner
# ==================================================

planner = Planner()

executor = PlanExecutor()

# ==================================================
# CREATE AUTOMATION
# ==================================================

print("\nTesting CREATE_AUTOMATION...")

intent = Intent(

    intent_type=IntentType.CREATE_AUTOMATION,

)

intent.set_parameter(
    "trigger",
    "time",
)

intent.set_parameter(
    "action",
    "backup",
)

intent.set_parameter(
    "target",
    "downloads",
)

plan = planner.create_plan(
    intent
)

assert plan.count() == 4

assert (
    plan.steps[0].name
    == "Validate Intent"
)

assert (
    plan.steps[1].name
    == "Create Trigger"
)

assert (
    plan.steps[2].name
    == "Create Action"
)

assert (
    plan.steps[3].name
    == "Register Automation"
)

print("PASS")

# ==================================================
# EXECUTION
# ==================================================

print("\nTesting Plan Execution...")

assert executor.execute(
    plan
)

assert plan.progress() == 100.0

assert (
    executor.executed_plans
    == 1
)

for step in plan:

    assert step.is_completed()

print("PASS")

# ==================================================
# RUN
# ==================================================

print("\nTesting RUN_AUTOMATION...")

intent = Intent(

    intent_type=IntentType.RUN_AUTOMATION,

)

plan = planner.create_plan(
    intent
)

assert plan.count() == 1

assert (
    plan.steps[0].name
    == "Run Automation"
)

print("PASS")

# ==================================================
# STOP
# ==================================================

print("\nTesting STOP_AUTOMATION...")

intent = Intent(

    intent_type=IntentType.STOP_AUTOMATION,

)

plan = planner.create_plan(
    intent
)

assert plan.count() == 1

assert (
    plan.steps[0].name
    == "Stop Automation"
)

print("PASS")

# ==================================================
# QUESTION
# ==================================================

print("\nTesting QUESTION...")

intent = Intent(

    intent_type=IntentType.QUESTION,

)

plan = planner.create_plan(
    intent
)

assert plan.count() == 1

assert (
    plan.steps[0].name
    == "Answer Question"
)

print("PASS")

# ==================================================
# UNKNOWN
# ==================================================

print("\nTesting UNKNOWN...")

intent = Intent(

    intent_type=IntentType.UNKNOWN,

)

plan = planner.create_plan(
    intent
)

assert plan.count() == 1

assert (
    plan.steps[0].name
    == "Unknown Intent"
)

print("PASS")

# ==================================================

print()

print(
    "Executed Plans :",
    executor.executed_plans,
)

print()

print("=" * 60)
print("ALL PLANNER TESTS PASSED")
print("=" * 60)
