"""
command_executor.py

Executes routed assistant commands.
"""

from __future__ import annotations

from automation.assistant.command import (
    Command,
)


class CommandExecutor:

    def __init__(self):

        self.executed = 0

    # ---------------------------- #

    def execute(

        self,

        command: Command,

        handler,

    ):

        if handler is None:

            command.fail()

            return False

        command.start()

        try:

            handler(command)

            command.complete()

            self.executed += 1

            return True

        except Exception:

            command.fail()

            return False

    # ---------------------------- #

    def count(self):

        return self.executed

    # ---------------------------- #

    def __repr__(self):

        return (

            "<CommandExecutor "

            f"executed={self.executed}>"

        )
