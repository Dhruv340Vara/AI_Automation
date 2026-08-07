"""
command_parser.py

Parse raw user input into normalized command text.
"""

from __future__ import annotations


class CommandParser:

    def __init__(self):

        pass

    # ---------------------------- #

    def parse(
        self,
        text: str,
    ) -> str:

        if not text:
            return ""

        # lowercase
        text = text.lower()

        # remove extra spaces
        text = " ".join(
            text.split()
        )

        return text

    # ---------------------------- #

    def tokenize(
        self,
        text: str,
    ):

        text = self.parse(text)

        return text.split()

    # ---------------------------- #

    def __repr__(self):

        return "<CommandParser>"