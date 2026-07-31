from __future__ import annotations
from automation.automation_manager import AutomationManager
from automation.automation_storage import AutomationStorage
from automation.automation_types import Automation

class AutomationCore:

    def __init__(
        self,
        storage_path="automation/data/automations.json"
    ):
        self.storage = AutomationStorage(storage_path)
        self.manager = AutomationManager(
            storage=self.storage
        )

    def create(
        self,
        name,
        description="",
        trigger=None,
        action=None,
        metadata=None
    ):
        automation = Automation(
            name=name,
            description=description,
            trigger=trigger or {},
            action=action or {},
            metadata=metadata or {}
        )
        self.manager.create_automation(
            automation
        )
        return automation

    def delete(
        self,
        automation_id
    ):
        return self.manager.delete_automation(
            automation_id
        )

    def get(
        self,
        automation_id
    ):
        return self.manager.get_automation(
            automation_id
        )

    def list(self):
        return self.manager.list_automations()

    def update(
        self,
        automation_id,
        **kwargs
    ):
        return self.manager.update_automation(
            automation_id,
            **kwargs
        )

    def enable(
        self,
        automation_id
    ):
        return self.manager.enable_automation(
            automation_id
        )

    def disable(
        self,
        automation_id
    ):
        return self.manager.disable_automation(
            automation_id
        )

    def exists(
        self,
        automation_id
    ):
        return self.manager.automation_exists(
            automation_id
        )

    def exists_name(
        self,
        name
    ):
        return self.manager.name_exists(
            name
        )

    def reload(self):
        return self.manager.load()

    def save(self):
        return self.manager.save()

    def count(self):
        return self.manager.count()

    def clear(self):
        self.manager.clear()

    def __len__(self):
        return len(self.manager)

    def __iter__(self):
        return iter(self.manager)
