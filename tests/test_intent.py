from automation.ai.intent import (
    Intent,
)

from automation.ai.intent_types import (
    IntentType,
)

intent = Intent(

    intent_type=IntentType.CREATE_AUTOMATION,

    confidence=0.96,

)

intent.set_parameter(

    "trigger",

    "time",

)

intent.set_parameter(

    "action",

    "backup",

)

intent.set_parameter(

    "target",

    "Downloads",

)

print(intent)

print()

print(intent.to_dict())

print()

copy = Intent.from_dict(

    intent.to_dict()

)

print(copy)

print(copy.intent_type)

print(copy.get_parameter("action"))

print(copy.has_parameter("target"))

print(copy.has_parameter("abc"))
