from __future__ import annotations

from typing import Dict, List, Optional

from automation.triggers.trigger import Trigger


class TriggerRegistry:

    def __init__(self):

        self._triggers: Dict[str, Trigger] = {}

    def register(
        self,
        trigger: Trigger,
    ):

        if trigger.trigger_id in self._triggers:

            raise ValueError(
                "Trigger already registered."
            )

        self._triggers[
            trigger.trigger_id
        ] = trigger

        return trigger

    def unregister(
        self,
        trigger_id: str,
    ):

        return self._triggers.pop(
            trigger_id,
            None,
        )

    def get(
        self,
        trigger_id: str,
    ) -> Optional[Trigger]:

        return self._triggers.get(
            trigger_id
        )

    def exists(
        self,
        trigger_id: str,
    ) -> bool:

        return trigger_id in self._triggers

    def all(self) -> List[Trigger]:

        return list(
            self._triggers.values()
        )

    def enabled(self):

        return [

            trigger

            for trigger in self._triggers.values()

            if trigger.enabled

        ]

    def disabled(self):

        return [

            trigger

            for trigger in self._triggers.values()

            if not trigger.enabled

        ]

    def clear(self):

        self._triggers.clear()

    def count(self):

        return len(
            self._triggers
        )

    def __len__(self):

        return self.count()

    def __iter__(self):

        return iter(
            self._triggers.values()
        )

    def __repr__(self):

        return (
            f"<TriggerRegistry "
            f"count={self.count()}>"
        )
