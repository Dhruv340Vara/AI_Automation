from __future__ import annotations

import re

from automation.ai.intent import (
    Intent,
)

from automation.ai.intent_matcher import (
    IntentMatcher,
)

from automation.ai.intent_types import (
    IntentType,
)


class IntentParser:
    """
    Parses user text into an Intent.
    """

    def __init__(
        self,
        matcher: IntentMatcher,
    ):

        self.matcher = matcher

    # -------------------------------- #

    def parse(
        self,
        text: str,
    ) -> Intent:

        intent_type = self.matcher.match(
            text
        )

        intent = Intent(
            intent_type=intent_type,
            confidence=1.0,
            source="rule",
        )

        self._extract_parameters(
            text,
            intent,
        )

        return intent

    # -------------------------------- #

    def _extract_parameters(
        self,
        text: str,
        intent: Intent,
    ):

        lower = text.lower()

        # ----------------------------
        # Trigger
        # ----------------------------

        if "every" in lower:

            intent.set_parameter(
                "trigger",
                "time",
            )

        if intent.intent_type == IntentType.RUN_AUTOMATION:
            intent.set_parameter(
                "action",
                "run",
            )
        elif intent.intent_type == IntentType.STOP_AUTOMATION:
            intent.set_parameter(
                "action",
                "stop",
            )
        else:
            actions = [
                "backup",
                "delete",
                "copy",
                "move",
            ]
            for action in actions:
                if action in lower:
                    intent.set_parameter(
                        "action",
                        action,
                    )
                    break

        schedules = [

            "every day",
            "every night",
            "daily",
            "weekly",
            "monthly",

        ]

        for schedule in schedules:

            if schedule in lower:

                intent.set_parameter(
                    "schedule",
                    schedule,
                )

                break

        # ----------------------------
        # Target
        # ----------------------------

        match = re.search(

            r"\b(downloads|documents|desktop|pictures|music|videos)\b",

            lower,

        )

        if match:

            intent.set_parameter(

                "target",

                match.group(1),

            )

    # -------------------------------- #

    def __repr__(self):

        return "<IntentParser>"
