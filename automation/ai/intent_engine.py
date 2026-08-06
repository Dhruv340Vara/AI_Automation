from __future__ import annotations

from automation.ai.intent import (
    Intent,
)

from automation.ai.intent_matcher import (
    IntentMatcher,
)

from automation.ai.intent_parser import (
    IntentParser,
)


class IntentEngine:
    """
    High-level intent engine.

    Coordinates matching and parsing.
    """

    def __init__(self):

        self.matcher = IntentMatcher()

        self.parser = IntentParser(
            self.matcher
        )

    # ---------------------------- #

    def add_rule(
        self,
        intent,
        *keywords,
    ):

        self.matcher.add_rule(
            intent,
            *keywords,
        )

    # ---------------------------- #

    def parse(
        self,
        text: str,
    ) -> Intent:

        return self.parser.parse(
            text
        )

    # ---------------------------- #

    def classify(
        self,
        text: str,
    ):

        return self.matcher.match(
            text
        )

    # ---------------------------- #

    def clear_rules(
        self,
    ):

        self.matcher.clear()

    # ---------------------------- #

    def rule_count(
        self,
    ):

        return self.matcher.count()

    # ---------------------------- #

    def __repr__(self):

        return (
            "<IntentEngine "
            f"rules={self.rule_count()}>"
        )
