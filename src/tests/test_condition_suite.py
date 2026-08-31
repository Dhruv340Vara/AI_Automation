from __future__ import annotations

print("=" * 60)
print("          CONDITION TEST SUITE")
print("=" * 60)

from automation.conditions.comparison_condition import (
    ComparisonCondition,
)

from automation.conditions.logical_condition import (
    LogicalCondition,
)

from automation.conditions.expression_condition import (
    ExpressionCondition,
)

from automation.conditions.condition_evaluator import (
    ConditionEvaluator,
)

from automation.automation_runtime import (
    AutomationRuntime,
)

from automation.events.event import (
    Event,
)

from automation.events.event_types import (
    EventType,
)

# ------------------------------------------------

battery = ComparisonCondition(
    name="Battery",
    key="battery",
    operator_symbol="<",
    expected=20,
)

wifi = ComparisonCondition(
    name="WiFi",
    key="wifi",
    operator_symbol="==",
    expected=True,
)

logical = LogicalCondition(
    name="Battery AND WiFi",
    operator="AND",
    conditions=[
        battery,
        wifi,
    ],
)

expression = ExpressionCondition(
    name="Expression",
    expression="battery < 20 and wifi == True",
)

# ------------------------------------------------

context = {
    "battery": 10,
    "wifi": True,
}

print("\nComparison")

assert battery(context) is True

print("PASS")

print("\nLogical")

assert logical(context) is True

print("PASS")

print("\nExpression")

assert expression(context) is True

print("PASS")

# ------------------------------------------------

evaluator = ConditionEvaluator()

evaluator.add(
    battery
)

evaluator.add(
    wifi
)

print("\nEvaluator")

assert evaluator.evaluate(
    context
) is True

details = evaluator.evaluate_all(
    context
)

print(details)

assert details["Battery"] is True

assert details["WiFi"] is True

print("PASS")

# ------------------------------------------------

runtime = AutomationRuntime()

runtime.add_condition(
    battery
)

runtime.add_condition(
    wifi
)

runtime.start()

event = Event(

    event_type=EventType.MANUAL,

    source="test",

    payload=context,

)

print("\nRuntime")

assert runtime.emit_event(
    event
) is True

runtime.stop()

print("PASS")

# ------------------------------------------------

print()

print("=" * 60)

print("ALL CONDITION TESTS PASSED")

print("=" * 60)
