"""
command_matcher.py

Simple rule-based command matcher.
"""

from __future__ import annotations


class CommandMatcher:

    def __init__(self):

        self._rules: dict[
            str,
            list[str],
        ] = {}

    # ---------------------------- #

    def register(
        self,
        command: str,
        *keywords: str,
    ):

        self._rules[
            command.lower()
        ] = [

            keyword.lower()

            for keyword in keywords

        ]

    # ---------------------------- #

    def match(
        self,
        text: str,
    ):

        lower = text.lower()

        best_command = None

        best_score = 0

        for command, keywords in self._rules.items():

            score = 0

            for keyword in keywords:

                if keyword in lower:

                    score += 1

            if score > best_score:

                best_score = score

                best_command = command

        return best_command

    # ---------------------------- #

    def rules(self):

        return self._rules

    # ---------------------------- #

    def clear(self):

        self._rules.clear()

    # ---------------------------- #

    def __len__(self):

        return len(self._rules)

    # ---------------------------- #

    def __repr__(self):

        return (

            "<CommandMatcher "

            f"rules={len(self)}>"

        )
