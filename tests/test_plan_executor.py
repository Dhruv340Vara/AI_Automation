from automation.ai.execution_plan import (
    ExecutionPlan,
)

from automation.ai.plan_executor import (
    PlanExecutor,
)

from automation.ai.plan_step import (
    PlanStep,
)

plan = ExecutionPlan(

    name="Backup",

)

plan.add_step(

    PlanStep(

        "Validate",

    )

)

plan.add_step(

    PlanStep(

        "Create Trigger",

    )

)

plan.add_step(

    PlanStep(

        "Create Action",

    )

)

executor = PlanExecutor()

print(executor)

print()

result = executor.execute(
    plan
)

print(result)

print()

for step in plan:

    print(step)

print()

print(plan.progress())

print()

print(executor)
