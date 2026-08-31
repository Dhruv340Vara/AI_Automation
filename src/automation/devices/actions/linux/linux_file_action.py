"""
linux_file_action.py

File system operations on Linux.
"""

from __future__ import annotations

from automation.devices.actions.device_action import (
    DeviceAction,
)

from automation.devices import (
    CommandRunner,
)


class LinuxFileAction(DeviceAction):

    def __init__(self):

        super().__init__(
            "file",
        )

        self.runner = CommandRunner()

    # ---------------------------- #

    def validate(
        self,
        request,
    ):

        operation = request.get_parameter("operation")

        return bool(operation)

    # ---------------------------- #

    def perform(
        self,
        request,
    ):

        operation = request.get_parameter("operation")

        path = request.get_parameter("path")

        target = request.get_parameter("target")

        # ---------------------------- #
        # CREATE FOLDER
        if operation == "mkdir":

            result = self.runner.run(
                ["mkdir", "-p", path]
            )

        # ---------------------------- #
        # DELETE FILE/FOLDER
        elif operation == "delete":

            result = self.runner.run(
                ["rm", "-rf", path]
            )

        # ---------------------------- #
        # MOVE FILE
        elif operation == "move":

            result = self.runner.run(
                ["mv", path, target]
            )

        # ---------------------------- #
        # RENAME (same as move)
        elif operation == "rename":

            result = self.runner.run(
                ["mv", path, target]
            )

        # ---------------------------- #
        # COPY FILE
        elif operation == "copy":

            result = self.runner.run(
                ["cp", "-r", path, target]
            )

        else:

            raise ValueError(
                f"Unknown file operation: {operation}"
            )

        # ---------------------------- #

        if result.failed:

            raise RuntimeError(
                result.stderr.strip()
                or "File operation failed"
            )

        return True
