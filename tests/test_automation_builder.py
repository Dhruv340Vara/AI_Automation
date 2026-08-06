from automation.ai.automation_builder import (
    AutomationBuilder,
)

from automation.ai.automation_template import (
    AutomationTemplate,
)

builder = AutomationBuilder()

template = AutomationTemplate(

    name="Night Backup",

    trigger="time",

    action="backup",

    target="downloads",

    schedule="every night",

)

template.set_metadata(

    "author",

    "AI",

)

automation = builder.build(
    template
)

print(builder)

print()

print(automation)

print()

print("Trigger:")
print(automation.trigger)

print()

print("Action:")
print(automation.action)

print()

print("Metadata:")
print(automation.metadata)

print()

print("Enabled:")
print(automation.is_enabled())

print()

print("Validation:")
print(automation.validate())

print()

print("Dictionary:")
print(automation.to_dict())
