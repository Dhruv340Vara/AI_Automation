from automation.ai.intent_engine import (
    IntentEngine,
)

from automation.ai.intent_types import (
    IntentType,
)

engine = IntentEngine()

engine.add_rule(

    IntentType.CREATE_AUTOMATION,

    "backup",

    "every",

)

engine.add_rule(

    IntentType.RUN_AUTOMATION,

    "run",

    "start",

)

engine.add_rule(

    IntentType.QUESTION,

    "what",

    "how",

    "why",

)

print(engine)

print()

print(

    engine.classify(

        "Backup my Downloads every night"

    )

)

print()

intent = engine.parse(

    "Backup my Downloads every night"

)

print(intent)

print()

print(intent.parameters)

print()

print(engine.rule_count())
