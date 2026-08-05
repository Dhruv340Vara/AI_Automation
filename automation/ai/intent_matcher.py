from __future__ import annotations
from automation.ai.intent_types import (
    IntentType,
)

class IntentMatcher:

    def __init__(self):
        self._rules = {}

    def add_rule(
        self,
        intent: IntentType,
        *keywords: str,
    ):
        words = [
            word.lower().strip()
            for word in keywords
        ]
        self._rules.setdefault(
            intent,
            set(),
        ).update(words)

    def remove_rule(
        self,
        intent: IntentType,
    ):
        return (
            self._rules.pop(
                intent,
                None,
            )
            is not None
        )

    def clear(self):
        self._rules.clear()

    def match(self,text: str,) -> IntentType:
        sentence = text.lower()
        best_intent = (IntentType.UNKNOWN)
        best_score = 0
        for intent, words in (self._rules.items()):
            score = 0
            for word in words:
                if word in sentence:
                    score += 1
            if score > best_score:
                best_score = score
                best_intent = intent
            elif (score == best_score and score > 0):
                best_intent = intent
        return best_intent

    def count(self):
        return len(
            self._rules
        )

    def __len__(self):
        return self.count()

    def __repr__(self):
        return (
            "<IntentMatcher "
            f"rules={self.count()}>"
        )
