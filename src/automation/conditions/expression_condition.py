from __future__ import annotations

import ast
import operator

from automation.conditions.condition import (
    Condition,
)


class ExpressionCondition(
    Condition,
):
    """
    Safely evaluates boolean expressions.

    Example:

    battery < 20 and wifi == True
    """

    OPERATORS = {

        ast.And: all,

        ast.Or: any,

        ast.Eq: operator.eq,

        ast.NotEq: operator.ne,

        ast.Gt: operator.gt,

        ast.GtE: operator.ge,

        ast.Lt: operator.lt,

        ast.LtE: operator.le,

    }

    def __init__(
        self,
        name: str,
        expression: str,
    ):

        super().__init__(name)

        self.expression = expression

    # -------------------------------- #

    def evaluate(
        self,
        context: dict,
    ) -> bool:

        tree = ast.parse(

            self.expression,

            mode="eval",

        )

        return self._evaluate_node(

            tree.body,

            context,

        )

    # -------------------------------- #

    def _evaluate_node(
        self,
        node,
        context,
    ):

        if isinstance(
            node,
            ast.BoolOp,
        ):

            values = [

                self._evaluate_node(
                    value,
                    context,
                )

                for value in node.values

            ]

            operation = self.OPERATORS[
                type(node.op)
            ]

            return operation(
                values
            )

        if isinstance(
            node,
            ast.Compare,
        ):

            left = self._evaluate_node(
                node.left,
                context,
            )

            right = self._evaluate_node(
                node.comparators[0],
                context,
            )

            operation = self.OPERATORS[
                type(node.ops[0])
            ]

            return operation(
                left,
                right,
            )

        if isinstance(
            node,
            ast.Name,
        ):

            return context.get(
                node.id
            )

        if isinstance(
            node,
            ast.Constant,
        ):

            return node.value

        raise ValueError(
            f"Unsupported node: {type(node).__name__}"
        )

    # -------------------------------- #

    def __repr__(self):

        return (
            "<ExpressionCondition "
            f"{self.expression}>"
        )
