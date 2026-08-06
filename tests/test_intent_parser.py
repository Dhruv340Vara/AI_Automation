from automation.ai.intent_matcher import (
    IntentMatcher,
)

from automation.ai.intent_parser import (
    IntentParser,
)

from automation.ai.intent_types import (
    IntentType,
)

matcher = IntentMatcher()

matcher.add_rule(

    IntentType.CREATE_AUTOMATION,

    "backup",

    "every",

)

matcher.add_rule(

    IntentType.RUN_AUTOMATION,

    "run",

    "start",

)

parser = IntentParser(
    matcher
)

intent = parser.parse(

    "Backup my Downloads every night"

)

print(intent)

print()

print(intent.intent_type)

print()

print(intent.parameters)

print()

print(intent.get_parameter("action"))

print(intent.get_parameter("target"))

print(intent.get_parameter("schedule"))

print(intent.get_parameter("trigger"))
