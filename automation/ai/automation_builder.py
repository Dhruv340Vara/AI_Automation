from __future__ import annotations

from automation.ai.automation_template import (
    AutomationTemplate,
)

from automation.automation_types import (
    Automation,
)


class AutomationBuilder:
    """
    Builds an Automation object
    from an AutomationTemplate.
    """

    def build(
        self,
        template: AutomationTemplate,
    ) -> Automation:

        automation = Automation(

            name=template.name,

            trigger={

                "type": template.trigger,

                "schedule": template.schedule,

            },

            action={

                "type": template.action,

                "target": template.target,

            },

            metadata=dict(
                template.metadata
            ),

        )

        automation.validate()

        return automation

    # ---------------------------- #

    def __repr__(self):

        return "<AutomationBuilder>"
