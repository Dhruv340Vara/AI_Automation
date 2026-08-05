from __future__ import annotations

print("=" * 60)
print("            AI INTENT TEST SUITE")
print("=" * 60)

from automation.ai.intent_engine import (
    IntentEngine,
)

from automation.ai.intent_types import (
    IntentType,
)

# ==================================================

engine = IntentEngine()

engine.add_rule(
    IntentType.CREATE_AUTOMATION,
    "backup",
    "every",
)

engine.add_rule(
    IntentType.RUN_AUTOMATION,
    "run",
    "execute",
    "start",
)

engine.add_rule(
    IntentType.STOP_AUTOMATION,
    "stop",
)

engine.add_rule(
    IntentType.QUESTION,
    "what",
    "why",
    "how",
)

# ==================================================
# CREATE AUTOMATION
# ==================================================

print("\nTesting CREATE_AUTOMATION...")

intent = engine.parse(
    "Backup my Downloads every night"
)

assert (
    intent.intent_type
    == IntentType.CREATE_AUTOMATION
)

assert (
    intent.get_parameter("action")
    == "backup"
)

assert (
    intent.get_parameter("trigger")
    == "time"
)

assert (
    intent.get_parameter("target")
    == "downloads"
)

assert (
    intent.get_parameter("schedule")
    == "every night"
)

print("PASS")

# ==================================================
# RUN
# ==================================================

print("\nTesting RUN_AUTOMATION...")

intent = engine.parse(
    "Run backup"
)

assert (
    intent.intent_type
    == IntentType.RUN_AUTOMATION
)

assert (
    intent.get_parameter("action")
    == "run"
)

print("PASS")

# ==================================================
# STOP
# ==================================================

print("\nTesting STOP_AUTOMATION...")

intent = engine.parse(
    "Stop automation"
)

assert (
    intent.intent_type
    == IntentType.STOP_AUTOMATION
)

assert (
    intent.get_parameter("action")
    == "stop"
)

print("PASS")

# ==================================================
# QUESTION
# ==================================================

print("\nTesting QUESTION...")

intent = engine.parse(
    "How are you?"
)

assert (
    intent.intent_type
    == IntentType.QUESTION
)

print("PASS")

# ==================================================
# UNKNOWN
# ==================================================

print("\nTesting UNKNOWN...")

intent = engine.parse(
    "abcdefghijk"
)

assert (
    intent.intent_type
    == IntentType.UNKNOWN
)

print("PASS")

# ==================================================

print()

print("Registered Rules :",
      engine.rule_count())

print()

print("=" * 60)
print("ALL AI INTENT TESTS PASSED")
print("=" * 60)
