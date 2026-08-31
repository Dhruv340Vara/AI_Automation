from __future__ import annotations

import operator

from automation.conditions.condition import (
    Condition,
)


class ComparisonCondition(
    Condition,
):
    """
    Generic comparison condition.
    """

    OPERATORS = {

        "==": operator.eq,

        "!=": operator.ne,

        ">": operator.gt,

        ">=": operator.ge,

        "<": operator.lt,

        "<=": operator.le,

    }

    def __init__(
        self,
        name: str,
        key: str,
        operator_symbol: str,
        expected,
    ):

        super().__init__(name)

        if operator_symbol not in self.OPERATORS:

            raise ValueError(
                f"Unsupported operator: {operator_symbol}"
            )

        self.key = key

        self.operator_symbol = operator_symbol

        self.expected = expected

    # ---------------------------- #

    def evaluate(
        self,
        context: dict,
    ):

        actual = context.get(
            self.key
        )

        operation = self.OPERATORS[
            self.operator_symbol
        ]

        try:

            return operation(
                actual,
                self.expected,
            )

        except Exception:

            return False

    # ---------------------------- #

    def __repr__(self):

        return (

            "<ComparisonCondition "

            f"{self.key} "

            f"{self.operator_symbol} "

            f"{self.expected}>"

        )
