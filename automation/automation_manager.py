"""
automation_manager.py

Manages all registered automations.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from automation.automation_types import Automation


class AutomationManager:
    """
    In-memory automation registry.
    """

    def __init__(self):

        self._automations: Dict[str, Automation] = {}

    # --------------------------------------------------
    # Create
    # --------------------------------------------------

    def create_automation(self, automation: Automation) -> None:

        automation.validate()

        if self.name_exists(automation.name):
            raise ValueError(
                f"Automation '{automation.name}' already exists."
            )

        self._automations[automation.automation_id] = automation

    # --------------------------------------------------
    # Delete
    # --------------------------------------------------

    def delete_automation(self, automation_id: str) -> bool:

        if automation_id not in self._automations:
            return False

        del self._automations[automation_id]

        return True

    # --------------------------------------------------
    # Get
    # --------------------------------------------------

    def get_automation(
        self,
        automation_id: str
    ) -> Optional[Automation]:

        return self._automations.get(automation_id)

    # --------------------------------------------------
    # List
    # --------------------------------------------------

    def list_automations(self) -> List[Automation]:

        return list(self._automations.values())

    # --------------------------------------------------
    # Exists
    # --------------------------------------------------

    def automation_exists(
        self,
        automation_id: str
    ) -> bool:

        return automation_id in self._automations

    def name_exists(
        self,
        name: str
    ) -> bool:

        target = name.strip().lower()

        for automation in self._automations.values():

            if automation.name.strip().lower() == target:
                return True

        return False

    # --------------------------------------------------
    # Enable / Disable
    # --------------------------------------------------

    def enable_automation(
        self,
        automation_id: str
    ) -> bool:

        automation = self.get_automation(automation_id)

        if automation is None:
            return False

        automation.enable()

        return True

    def disable_automation(
        self,
        automation_id: str
    ) -> bool:

        automation = self.get_automation(automation_id)

        if automation is None:
            return False

        automation.disable()

        return True

    # --------------------------------------------------
    # Update
    # --------------------------------------------------

    def update_automation(
        self,
        automation_id: str,
        **kwargs
    ) -> bool:

        automation = self.get_automation(automation_id)

        if automation is None:
            return False

        allowed_fields = {
            "name",
            "description",
            "trigger",
            "action",
            "metadata",
        }

        for key, value in kwargs.items():

            if key not in allowed_fields:
                continue

            if key == "name":

                new_name = str(value).strip()

                if (
                    new_name.lower()
                    != automation.name.lower()
                    and self.name_exists(new_name)
                ):
                    raise ValueError(
                        "Automation name already exists."
                    )

            setattr(automation, key, value)

        automation.validate()

        automation.touch()

        return True

    # --------------------------------------------------
    # Utilities
    # --------------------------------------------------

    def clear(self):

        self._automations.clear()

    def count(self):

        return len(self._automations)

    def __len__(self):

        return len(self._automations)

    def __iter__(self):

        return iter(self._automations.values())
