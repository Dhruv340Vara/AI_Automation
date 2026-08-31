"""
command_registry.py

Stores all available assistant commands.
"""

from __future__ import annotations

from typing import Callable


class CommandRegistry:

    def __init__(self):

        self._commands: dict[
            str,
            Callable,
        ] = {}

    # ---------------------------- #

    def register(
        self,
        name: str,
        handler: Callable,
    ):

        self._commands[
            name.lower()
        ] = handler

    # ---------------------------- #

    def unregister(
        self,
        name: str,
    ):

        self._commands.pop(
            name.lower(),
            None,
        )

    # ---------------------------- #

    def get(
        self,
        name: str,
    ):

        return self._commands.get(
            name.lower()
        )

    # ---------------------------- #

    def exists(
        self,
        name: str,
    ):

        return (
            name.lower()
            in self._commands
        )

    # ---------------------------- #

    def names(
        self,
    ):

        return sorted(
            self._commands.keys()
        )

    # ---------------------------- #

    def count(
        self,
    ):

        return len(
            self._commands
        )

    # ---------------------------- #

    def clear(
        self,
    ):

        self._commands.clear()

    # ---------------------------- #

    def __len__(
        self,
    ):

        return self.count()

    # ---------------------------- #

    def __repr__(
        self,
    ):

        return (
            "<CommandRegistry "
            f"commands={self.count()}>"
        )
