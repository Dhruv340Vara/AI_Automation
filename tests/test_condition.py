from automation.conditions.condition import (
    Condition,
)


class DemoCondition(
    Condition,
):

    def evaluate(
        self,
        context,
    ):

        return context.get(
            "value",
            0,
        ) > 10


condition = DemoCondition(
    "Greater Than 10",
)

print(condition)

print(
    condition(
        {
            "value": 15,
        }
    )
)

print(
    condition(
        {
            "value": 5,
        }
    )
)

condition.disable()

print(
    condition.is_enabled()
)

print(
    condition(
        {
            "value": 100,
        }
    )
)

condition.enable()

print(
    condition.is_enabled()
)

print(
    condition(
        {
            "value": 100,
        }
    )
)
