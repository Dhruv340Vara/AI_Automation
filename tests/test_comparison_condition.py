from automation.conditions.comparison_condition import (
    ComparisonCondition,
)

condition = ComparisonCondition(

    name="Battery Low",

    key="battery",

    operator_symbol="<",

    expected=20,

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

            "battery": 50,

        }

    )

)

print("-" * 40)

price = ComparisonCondition(

    name="Price",

    key="price",

    operator_symbol=">",

    expected=100,

)

print(

    price(

        {

            "price": 150,

        }

    )

)

print(

    price(

        {

            "price": 80,

        }

    )

)

print("-" * 40)

extension = ComparisonCondition(

    name="Extension",

    key="extension",

    operator_symbol="==",

    expected="pdf",

)

print(

    extension(

        {

            "extension": "pdf",

        }

    )

)

print(

    extension(

        {

            "extension": "jpg",

        }

    )

)
