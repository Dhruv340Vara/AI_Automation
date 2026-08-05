from automation.ai.intent_types import (
    IntentType,
)

print(IntentType.CHAT)

print(IntentType.CREATE_AUTOMATION)

print()

print(IntentType.values())

print()

print(IntentType.names())

print()

print(
    IntentType.has_value(
        "chat"
    )
)

print(
    IntentType.has_value(
        "abc"
    )
)
