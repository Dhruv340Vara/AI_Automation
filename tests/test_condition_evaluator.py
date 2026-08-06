from automation.conditions.comparison_condition import (
    ComparisonCondition,
)

from automation.conditions.logical_condition import (
    LogicalCondition,
)

from automation.conditions.condition_evaluator import (
    ConditionEvaluator,
)

battery = ComparisonCondition(

    name="Battery",

    key="battery",

    operator_symbol="<",

    expected=20,

)

wifi = ComparisonCondition(

    name="WiFi",

    key="wifi",

    operator_symbol="==",

    expected=True,

)

logical = LogicalCondition(

    name="Battery AND WiFi",

    operator="AND",

    conditions=[

        battery,

        wifi,

    ],

)

evaluator = ConditionEvaluator()

evaluator.add(
    battery
)

evaluator.add(
    wifi
)

print(evaluator)

print("-" * 50)

context = {

    "battery": 10,

    "wifi": True,

}

print(

    evaluator.evaluate(
        context
    )

)

print(

    evaluator.evaluate_all(
        context
    )

)

print("-" * 50)

context = {

    "battery": 50,

    "wifi": True,

}

print(

    evaluator.evaluate(
        context
    )

)

print(

    evaluator.evaluate_all(
        context
    )

)

print("-" * 50)

evaluator.clear()

evaluator.add(
    logical
)

context = {

    "battery": 10,

    "wifi": True,

}

print(

    evaluator.evaluate(
        context
    )

)

print(

    evaluator.evaluate_all(
        context
    )

)
