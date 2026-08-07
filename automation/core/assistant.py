"""
assistant.py

Full integration of command system.
"""

from __future__ import annotations

from automation.commands.command_parser import CommandParser
from automation.commands.command_matcher import CommandMatcher
from automation.commands.command_mapper import CommandMapper

from automation.devices.actions.linux.linux_action_suite import (
    LinuxActionSuite,
)


class Assistant:

    def __init__(self):

        self.parser = CommandParser()
        self.matcher = CommandMatcher()
        self.mapper = CommandMapper()

        self.actions = LinuxActionSuite()

    # ---------------------------- #

    def handle(
        self,
        text: str,
    ):

        print("\nUSER :", text)

        # 1. Parse
        tokens = self.parser.tokenize(text)

        # 2. Match
        action = self.matcher.match(tokens)

        if not action:
            print("❌ Unknown command")
            return None

        # 3. Map
        request = self.mapper.map(action, tokens)

        if not request:
            print("❌ Failed to map command")
            return None

        # 4. Execute
        result = self.actions.registry.execute(request)

        print("✅ Result :", result)

        return result

    # ---------------------------- #

    def __repr__(self):

        return "<Assistant>"
