from automation.ai.execution_plan import (
    ExecutionPlan,
)

from automation.ai.plan_step import (
    PlanStep,
)

plan = ExecutionPlan(

    name="Backup Plan",

    description="Night Backup",

)

step1 = PlanStep(
    "Create Trigger"
)

step2 = PlanStep(
    "Create Action"
)

step3 = PlanStep(
    "Register Automation"
)

plan.add_step(step1)

plan.add_step(step2)

plan.add_step(step3)

print(plan)

print()

print(plan.count())

print(plan.progress())

print()

step1.complete()

print(plan.progress())

print()

step2.complete()

step3.complete()

print(plan.progress())

print()

print(plan.to_dict())

print()

copy = ExecutionPlan.from_dict(
    plan.to_dict()
)

print(copy)

print(copy.count())
