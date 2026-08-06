"""
command_router.py

Routes commands to their registered handlers.
"""

from __future__ import annotations

from automation.assistant.command import Command
from automation.assistant.command_matcher import CommandMatcher
from automation.assistant.command_registry import CommandRegistry


class CommandRouter:

    def __init__(
        self,
        matcher: CommandMatcher,
        registry: CommandRegistry,
    ):

        self.matcher = matcher
        self.registry = registry

    # ---------------------------- #

    def route(
        self,
        command: Command,
    ):

        command_name = self.matcher.match(
            command.description
        )

        if command_name is None:
            return None

        return self.registry.get(
            command_name
        )

    # ---------------------------- #

    def can_route(
        self,
        command: Command,
    ):

        return (
            self.route(command)
            is not None
        )

    # ---------------------------- #

    def __repr__(self):

        return (
            "<CommandRouter>"
        )
