from __future__ import annotations

from automation.ai.execution_plan import (
    ExecutionPlan,
)


class PlanExecutor:
    """
    Executes an ExecutionPlan.

    Future versions will connect
    with AutomationRuntime.
    """

    def __init__(self):

        self.executed_plans = 0

    # -------------------------------- #

    def execute(
        self,
        plan: ExecutionPlan,
    ):

        for step in plan:

            step.start()

            success = self.execute_step(
                step
            )

            if success:

                step.complete()

            else:

                step.fail()

                return False

        self.executed_plans += 1

        return True

    # -------------------------------- #

    def execute_step(
        self,
        step,
    ):

        """
        Placeholder execution.

        Phase 7.4 will replace this
        with Runtime integration.
        """

        return True

    # -------------------------------- #

    def reset(self):

        self.executed_plans = 0

    # -------------------------------- #

    def __repr__(self):

        return (

            "<PlanExecutor "

            f"executed={self.executed_plans}>"

        )
