from automation.ai.intent import (
    Intent,
)

from automation.ai.intent_types import (
    IntentType,
)

from automation.ai.planner import (
    Planner,
)

planner = Planner()

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

plan = planner.create_plan(
    intent
)

print(plan)

print()

for step in plan:

    print(step)

print()

print(plan.count())
