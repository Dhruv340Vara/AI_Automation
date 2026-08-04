from __future__ import annotations

from automation.triggers.trigger_registry import (
    TriggerRegistry,
)

from automation.triggers.trigger_storage import (
    TriggerStorage,
)


class TriggerEngine:

    def __init__(

        self,

        storage_path="data/triggers.json",

    ):

        self.storage = TriggerStorage(

            storage_path

        )

        self.registry = TriggerRegistry(

            storage=self.storage

        )

    def register(

        self,

        trigger,

    ):

        return self.registry.register(

            trigger

        )

    def unregister(

        self,

        trigger_id,

    ):

        return self.registry.unregister(

            trigger_id

        )

    def all(self):

        return self.registry.all()

    def enabled(self):

        return self.registry.enabled()

    def disabled(self):

        return self.registry.disabled()

    def count(self):

        return self.registry.count()
