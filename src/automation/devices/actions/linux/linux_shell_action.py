"""
linux_shell_action.py

Execute shell commands on Linux.
"""

from __future__ import annotations

from automation.devices.actions.device_action import (
    DeviceAction,
)

from automation.devices import (
    CommandRunner,
)


class LinuxShellAction(DeviceAction):

    def __init__(self):

        super().__init__(
            "shell",
        )

        self.runner = CommandRunner()

    # ---------------------------- #

    def validate(
        self,
        request,
    ):

        command = request.get_parameter(
            "command",
        )

        return bool(command)

    # ---------------------------- #

    def perform(
        self,
        request,
    ):

        command = request.get_parameter(
            "command",
        )

        # જો string હોય તો shell mode
        if isinstance(command, str):

            result = self.runner.shell(
                command
            )

        else:
            # list command
            result = self.runner.run(
                command
            )

        if result.failed:

            raise RuntimeError(
                result.stderr.strip()
                or "Command failed"
            )

        return result.stdout.strip()
