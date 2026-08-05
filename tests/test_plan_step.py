from automation.ai.plan_step import (
    PlanStep,
)

step = PlanStep(

    name="Create Trigger",

    description="Create a time trigger",

)

step.set_parameter(

    "time",

    "22:00",

)

print(step)

print()

print(step.to_dict())

print()

step.start()

print(step.status)

step.complete()

print(step.status)

step.reset()

print(step.status)

copy = PlanStep.from_dict(
    step.to_dict()
)

print()

print(copy)

print(copy.get_parameter("time"))
