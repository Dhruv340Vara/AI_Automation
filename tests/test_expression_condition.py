from automation.conditions.expression_condition import (
    ExpressionCondition,
)

condition = ExpressionCondition(

    "Battery",

    "battery < 20",

)

print(condition)

print(

    condition(

        {

            "battery": 10,

        }

    )

)

print(

    condition(

        {

            "battery": 40,

        }

    )

)

print("-" * 50)

condition = ExpressionCondition(

    "Battery And Wifi",

    "battery < 20 and wifi == True",

)

print(

    condition(

        {

            "battery": 10,

            "wifi": True,

        }

    )

)

print(

    condition(

        {

            "battery": 10,

            "wifi": False,

        }

    )

)

print("-" * 50)

condition = ExpressionCondition(

    "Complex",

    "battery < 20 or charging == True",

)

print(

    condition(

        {

            "battery": 50,

            "charging": True,

        }

    )

)

print(

    condition(

        {

            "battery": 50,

            "charging": False,

        }

    )

)
