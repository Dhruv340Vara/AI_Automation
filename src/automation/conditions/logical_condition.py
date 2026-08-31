from __future__ import annotations

from automation.conditions.condition import (
    Condition,
)


class LogicalCondition(
    Condition,
):
    """
    Combines multiple conditions
    using logical operators.
    """

    def __init__(
        self,
        name: str,
        operator: str,
        conditions: list[Condition],
    ):

        super().__init__(name)

        operator = operator.upper()

        if operator not in (
            "AND",
            "OR",
            "NOT",
        ):
            raise ValueError(
                f"Unsupported logical operator: {operator}"
            )

        if (
            operator == "NOT"
            and len(conditions) != 1
        ):
            raise ValueError(
                "NOT requires exactly one condition."
            )

        self.operator = operator

        self.conditions = conditions

    # -------------------------------- #

    def evaluate(
        self,
        context: dict,
    ) -> bool:

        results = [

            condition(context)

            for condition in self.conditions

        ]

        if self.operator == "AND":

            return all(results)

        if self.operator == "OR":

            return any(results)

        if self.operator == "NOT":

            return not results[0]

        return False

    # -------------------------------- #

    def __len__(self):

        return len(
            self.conditions
        )

    # -------------------------------- #

    def __repr__(self):

        return (
            "<LogicalCondition "
            f"{self.operator} "
            f"conditions={len(self)}>"
        )
