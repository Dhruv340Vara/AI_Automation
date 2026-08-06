from __future__ import annotations

from automation.ai.execution_plan import (ExecutionPlan,)
from automation.ai.automation_template import (AutomationTemplate,)
from automation.ai.automation_builder import (AutomationBuilder,)

class AutomationGenerator:

    def __init__(self):
        self.builder = AutomationBuilder()

    def generate(self,plan: ExecutionPlan,):
        template = self.create_template(plan)
        return self.builder.build(template)

    def create_template(self,plan: ExecutionPlan,) -> AutomationTemplate:
        template = AutomationTemplate(name=plan.name,)
        for step in plan:
            if step.name == "Create Trigger":
                template.trigger = step.get_parameter("trigger")
                template.schedule = step.get_parameter("schedule")
            elif step.name == "Create Action":
                template.action = step.get_parameter("action")
                template.target = step.get_parameter("target")
            elif step.name == "Register Automation":
                pass
        return template

    def __repr__(self):
        return "<AutomationGenerator>"
