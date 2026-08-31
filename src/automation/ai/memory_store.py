from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class MemoryStore:
    """
    Persistent JSON storage for AI memory.
    """

    def __init__(
        self,
        file_path: str = "memory/memory.json",
    ):

        self.file_path = Path(file_path)

        self.file_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        if not self.file_path.exists():

            self.save({})

    # -------------------------------- #

    def load(self) -> dict[str, Any]:

        try:

            with open(
                self.file_path,
                "r",
                encoding="utf-8",
            ) as file:

                return json.load(file)

        except (
            FileNotFoundError,
            json.JSONDecodeError,
        ):

            return {}

    # -------------------------------- #

    def save(
        self,
        data: dict[str, Any],
    ):

        with open(
            self.file_path,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False,
            )

    # -------------------------------- #

    def clear(self):

        self.save({})

    # -------------------------------- #

    def exists(self) -> bool:

        return self.file_path.exists()

    # -------------------------------- #

    def __repr__(self):

        return (
            "<MemoryStore "
            f"{self.file_path}>"
        )