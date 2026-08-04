from __future__ import annotations
from typing import Dict, List, Optional
from automation.triggers.trigger import Trigger

class TriggerRegistry:

    def __init__(self,storage=None,):
        self._triggers = {}
        self.storage = storage
        if self.storage is not None:
            self.load()

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
        self.save()
        return trigger

    def unregister(self,trigger_id: str,):
        trigger = self._triggers.pop(trigger_id,None,)
        self.save()
        return trigger

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
        self.save()

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

    def save(self):
        if self.storage is None:
            return False
        return self.storage.save(self.all())


    def load(self):
        if self.storage is None:
            return []
        triggers = self.storage.load()
        self._triggers.clear()
        for trigger in triggers:
            self._triggers[trigger.trigger_id] = trigger
        return triggers
