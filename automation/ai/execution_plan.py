from __future__ import annotations

from dataclasses import dataclass, field

from automation.ai.plan_step import (
    PlanStep,
)


@dataclass(slots=True)
class ExecutionPlan:
    """
    Represents a complete execution plan.
    """

    name: str

    description: str = ""

    steps: list[PlanStep] = field(
        default_factory=list
    )

    metadata: dict = field(
        default_factory=dict
    )

    # -------------------------------- #

    def add_step(
        self,
        step: PlanStep,
    ):

        self.steps.append(step)

    # -------------------------------- #

    def remove_step(
        self,
        index: int,
    ):

        return self.steps.pop(index)

    # -------------------------------- #

    def clear(self):

        self.steps.clear()

    # -------------------------------- #

    def count(self):

        return len(
            self.steps
        )

    # -------------------------------- #

    def completed_steps(self):

        return sum(

            step.is_completed()

            for step in self.steps

        )

    # -------------------------------- #

    def failed_steps(self):

        return sum(

            step.is_failed()

            for step in self.steps

        )

    # -------------------------------- #

    def pending_steps(self):

        return sum(

            step.is_pending()

            for step in self.steps

        )

    # -------------------------------- #

    def running_steps(self):

        return sum(

            step.is_running()

            for step in self.steps

        )

    # -------------------------------- #

    def progress(self):

        if not self.steps:

            return 0.0

        return (

            self.completed_steps()

            / len(self.steps)

        ) * 100

    # -------------------------------- #

    def to_dict(self):

        return {

            "name": self.name,

            "description": self.description,

            "metadata": self.metadata,

            "steps": [

                step.to_dict()

                for step in self.steps

            ],

        }

    # -------------------------------- #

    @classmethod
    def from_dict(
        cls,
        data: dict,
    ):

        plan = cls(

            name=data["name"],

            description=data.get(
                "description",
                "",
            ),

            metadata=data.get(
                "metadata",
                {},
            ),

        )

        for item in data.get(
            "steps",
            [],
        ):

            plan.add_step(

                PlanStep.from_dict(
                    item
                )

            )

        return plan

    # -------------------------------- #

    def __len__(self):

        return len(
            self.steps
        )

    # -------------------------------- #

    def __iter__(self):

        return iter(
            self.steps
        )

    # -------------------------------- #

    def __repr__(self):

        return (

            "<ExecutionPlan "

            f"{self.name} "

            f"steps={len(self.steps)}>"

        )
