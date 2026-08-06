from __future__ import annotations

from automation.triggers.trigger import Trigger
from automation.triggers.trigger_types import (
    TriggerType,
)


class ManualTrigger(Trigger):
    """
    Trigger executed manually by
    user, UI, CLI or AI.
    """

    def __init__(
        self,
        name: str,
        description: str = "",
        metadata: dict | None = None,
    ):

        super().__init__(
            trigger_type=TriggerType.MANUAL,
            name=name,
            metadata=metadata or {},
        )

        self.description = description

    # ---------------------------- #

    def activate(self):

        return True

    # ---------------------------- #

    def __repr__(self):

        return (
            "<ManualTrigger "
            f"{self.name}>"
        )
