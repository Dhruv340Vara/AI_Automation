from __future__ import annotations

from automation.ai.tool import (
    Tool,
)


class ToolRegistry:
    """
    Stores and manages AI tools.
    """

    def __init__(self):

        self._tools: dict[str, Tool] = {}

    # -------------------------------- #

    def register(
        self,
        tool: Tool,
    ):

        self._tools[
            tool.name
        ] = tool

        return tool

    # -------------------------------- #

    def unregister(
        self,
        name: str,
    ):

        return self._tools.pop(
            name,
            None,
        )

    # -------------------------------- #

    def get(
        self,
        name: str,
    ):

        return self._tools.get(
            name,
        )

    # -------------------------------- #

    def exists(
        self,
        name: str,
    ):

        return (
            name
            in self._tools
        )

    # -------------------------------- #

    def tools(
        self,
    ):

        return list(
            self._tools.values()
        )

    # -------------------------------- #

    def names(
        self,
    ):

        return list(
            self._tools.keys()
        )

    # -------------------------------- #

    def count(
        self,
    ):

        return len(
            self._tools
        )

    # -------------------------------- #

    def clear(
        self,
    ):

        self._tools.clear()

    # -------------------------------- #

    def __repr__(self):

        return (
            f"<ToolRegistry "
            f"tools={self.count()}>"
        )
