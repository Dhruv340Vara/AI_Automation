from automation.conditions.comparison_condition import (
    ComparisonCondition,
)

from automation.conditions.logical_condition import (
    LogicalCondition,
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

print("-" * 50)

and_condition = LogicalCondition(

    name="Battery AND WiFi",

    operator="AND",

    conditions=[

        battery,

        wifi,

    ],

)

print(and_condition)

print(

    and_condition(

        {

            "battery": 10,

            "wifi": True,

        }

    )

)

print(

    and_condition(

        {

            "battery": 50,

            "wifi": True,

        }

    )

)

print("-" * 50)

or_condition = LogicalCondition(

    name="Battery OR WiFi",

    operator="OR",

    conditions=[

        battery,

        wifi,

    ],

)

print(

    or_condition(

        {

            "battery": 10,

            "wifi": False,

        }

    )

)

print(

    or_condition(

        {

            "battery": 50,

            "wifi": False,

        }

    )

)

print("-" * 50)

not_condition = LogicalCondition(

    name="NOT Battery",

    operator="NOT",

    conditions=[

        battery,

    ],

)

print(

    not_condition(

        {

            "battery": 10,

        }

    )

)

print(

    not_condition(

        {

            "battery": 50,

        }

    )

)
