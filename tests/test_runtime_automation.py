from automation.automation_runtime import (
    AutomationRuntime,
)

from automation.ai.execution_plan import (
    ExecutionPlan,
)

from automation.ai.plan_step import (
    PlanStep,
)

runtime = AutomationRuntime()

runtime.start()

plan = ExecutionPlan(

    name="Night Backup",

)

trigger = PlanStep(
    "Create Trigger"
)

trigger.set_parameter(
    "trigger",
    "time",
)

trigger.set_parameter(
    "schedule",
    "every night",
)

action = PlanStep(
    "Create Action"
)

action.set_parameter(
    "action",
    "backup",
)

action.set_parameter(
    "target",
    "downloads",
)

plan.add_step(trigger)

plan.add_step(action)

automation = runtime.generate_automation(
    plan
)

print(automation)

print()

print(runtime.automation_count())

print()

print(runtime.automations())

runtime.stop()
