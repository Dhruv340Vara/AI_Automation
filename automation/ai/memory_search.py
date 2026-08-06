from __future__ import annotations

from typing import Any


class MemorySearch:
    """
    Search utility for AI memory.
    """

    def find(
        self,
        data: dict[str, Any],
        key: str,
        default=None,
    ):

        return data.get(
            key,
            default,
        )

    # -------------------------------- #

    def exists(
        self,
        data: dict[str, Any],
        key: str,
    ) -> bool:

        return key in data

    # -------------------------------- #

    def keys(
        self,
        data: dict[str, Any],
    ):

        return list(
            data.keys()
        )

    # -------------------------------- #

    def values(
        self,
        data: dict[str, Any],
    ):

        return list(
            data.values()
        )

    # -------------------------------- #

    def search(
        self,
        data: dict[str, Any],
        keyword: str,
    ) -> dict[str, Any]:

        keyword = keyword.lower()

        result = {}

        for key, value in data.items():

            if keyword in key.lower():

                result[key] = value

                continue

            if keyword in str(value).lower():

                result[key] = value

        return result

    # -------------------------------- #

    def __repr__(self):

        return "<MemorySearch>"
