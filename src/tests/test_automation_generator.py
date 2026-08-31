from automation.ai.execution_plan import (
    ExecutionPlan,
)

from automation.ai.plan_step import (
    PlanStep,
)

from automation.ai.automation_generator import (
    AutomationGenerator,
)

plan = ExecutionPlan(

    name="Night Backup",

)

trigger = PlanStep(

    "Create Trigger",

)

trigger.set_parameter(

    "trigger",

    "time",

)

action = PlanStep(

    "Create Action",

)

action.set_parameter(

    "action",

    "backup",

)

plan.add_step(

    trigger

)

plan.add_step(

    action

)

generator = AutomationGenerator()

automation = generator.generate(
    plan
)

print(generator)

print()

print(automation)

print()

print(automation.trigger)

print()

print(automation.action)

print()

print(automation.metadata)
