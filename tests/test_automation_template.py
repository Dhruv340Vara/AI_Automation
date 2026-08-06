from automation.ai.automation_template import (
    AutomationTemplate,
)

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

print(template)

print()

print(template.to_dict())

print()

copy = AutomationTemplate.from_dict(

    template.to_dict()

)

print(copy)

print(copy.get_metadata("author"))
