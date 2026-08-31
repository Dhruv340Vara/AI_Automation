"""
command_mapper.py

Map command text to DeviceRequest.
"""

from __future__ import annotations

from automation.devices import DeviceRequest


class CommandMapper:

    def __init__(self):

        pass

    # ---------------------------- #

    def map(
        self,
        action: str,
        tokens: list[str],
    ) -> DeviceRequest | None:

        if not action:
            return None

        request = DeviceRequest(
            action=action
        )

        # ---------------------------- #
        # OPEN APP

        if action == "open_app":

            # open firefox
            if len(tokens) >= 2:
                request.set_parameter(
                    "app",
                    tokens[1]
                )

        # ---------------------------- #
        # SHELL COMMAND

        elif action == "shell":

            # run pwd
            if len(tokens) >= 2:
                request.set_parameter(
                    "command",
                    tokens[1:]
                )

        # ---------------------------- #
        # FILE OPERATIONS

        elif action == "file":

            operation = tokens[0]

            request.set_parameter(
                "operation",
                self._map_file_operation(operation)
            )

            # create folder test
            if len(tokens) >= 3:
                request.set_parameter(
                    "path",
                    tokens[2]
                )

            # move file a b
            if len(tokens) >= 4:
                request.set_parameter(
                    "target",
                    tokens[3]
                )

        return request

    # ---------------------------- #

    def _map_file_operation(
        self,
        word: str,
    ) -> str:

        mapping = {

            "create": "mkdir",
            "make": "mkdir",

            "delete": "delete",
            "remove": "delete",

            "copy": "copy",
            "move": "move",
            "rename": "rename",
        }

        return mapping.get(word, word)

    # ---------------------------- #

    def __repr__(self):

        return "<CommandMapper>"
