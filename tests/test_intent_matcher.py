from automation.ai.intent_matcher import (
    IntentMatcher,
)

from automation.ai.intent_types import (
    IntentType,
)

matcher = IntentMatcher()

matcher.add_rule(

    IntentType.CREATE_AUTOMATION,

    "create",

    "backup",

    "every",

)

matcher.add_rule(

    IntentType.RUN_AUTOMATION,

    "run",

    "execute",

    "start",

)

matcher.add_rule(

    IntentType.QUESTION,

    "what",

    "why",

    "how",

)

print(matcher)

print()

print(

    matcher.match(

        "Backup my Downloads every night"

    )

)

print(

    matcher.match(

        "Run backup"

    )

)

print(

    matcher.match(

        "How are you?"

    )

)

print(

    matcher.match(

        "abcdef"

    )

)

print()

print(len(matcher))
