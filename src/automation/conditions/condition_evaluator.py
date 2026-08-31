from __future__ import annotations

from automation.conditions.condition import (
    Condition,
)


class ConditionEvaluator:
    """
    Evaluates one or more conditions.
    """

    def __init__(self):

        self._conditions = []

    # -------------------------------- #

    def add(
        self,
        condition: Condition,
    ):

        self._conditions.append(
            condition
        )

        return condition

    # -------------------------------- #

    def remove(
        self,
        condition: Condition,
    ):

        if condition in self._conditions:

            self._conditions.remove(
                condition
            )

            return True

        return False

    # -------------------------------- #

    def clear(self):

        self._conditions.clear()

    # -------------------------------- #

    def evaluate(
        self,
        context: dict,
    ) -> bool:

        for condition in self._conditions:

            if not condition(context):

                return False

        return True

    # -------------------------------- #

    def evaluate_all(
        self,
        context: dict,
    ):

        return {

            condition.name: condition(
                context
            )

            for condition in self._conditions

        }

    # -------------------------------- #

    def count(self):

        return len(
            self._conditions
        )

    # -------------------------------- #

    def __len__(self):

        return self.count()

    # -------------------------------- #

    def __iter__(self):

        return iter(
            self._conditions
        )

    # -------------------------------- #

    def __repr__(self):

        return (
            "<ConditionEvaluator "
            f"conditions={self.count()}>"
        )
