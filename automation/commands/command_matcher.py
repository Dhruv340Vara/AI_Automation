"""
command_matcher.py

Match parsed command text to action type.
"""

from __future__ import annotations


class CommandMatcher:

    def __init__(self):

        # keyword आधारित mapping
        self.rules = {

            "open": "open_app",
            "launch": "open_app",
            "start": "open_app",

            "run": "shell",
            "execute": "shell",

            "create": "file",
            "make": "file",
            "delete": "file",
            "remove": "file",
            "copy": "file",
            "move": "file",
            "rename": "file",
        }

    # ---------------------------- #

    def match(
        self,
        tokens: list[str],
    ) -> str | None:

        if not tokens:
            return None

        first_word = tokens[0]

        return self.rules.get(first_word)

    # ---------------------------- #

    def __repr__(self):

        return "<CommandMatcher>"
