"""
automation_storage.py

JSON storage backend for automations.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import List

from automation.automation_types import Automation


class AutomationStorage:
    """
    Handles saving and loading automations
    from a JSON file.
    """

    def __init__(self, file_path: str):

        self.file_path = Path(file_path)

        self._ensure_storage()

    # --------------------------------------------------
    # Internal
    # --------------------------------------------------

    def _ensure_storage(self):
        """
        Create directory and JSON file if missing.
        """

        self.file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        if not self.file_path.exists():

            with open(
                self.file_path,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    [],
                    file,
                    indent=4
                )

    # --------------------------------------------------
    # Save
    # --------------------------------------------------

    def save(
        self,
        automations: List[Automation]
    ) -> bool:

        data = [
            automation.to_dict()
            for automation in automations
        ]

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        return True

    # --------------------------------------------------
    # Load
    # --------------------------------------------------

    def load(self) -> List[Automation]:

        self._ensure_storage()

        try:

            with open(
                self.file_path,
                "r",
                encoding="utf-8"
            ) as file:

                raw = json.load(file)

        except json.JSONDecodeError:

            return []

        automations = []

        for item in raw:

            try:

                automations.append(
                    Automation.from_dict(item)
                )

            except Exception:

                continue

        return automations

    # --------------------------------------------------
    # Clear
    # --------------------------------------------------

    def clear(self):

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                [],
                file,
                indent=4
            )

    # --------------------------------------------------
    # Count
    # --------------------------------------------------

    def count(self):

        return len(
            self.load()
        )

    # --------------------------------------------------
    # Exists
    # --------------------------------------------------

    def exists(self):

        return self.file_path.exists()

    # --------------------------------------------------
    # Backup
    # --------------------------------------------------

    def backup(
        self,
        backup_path: str
    ):

        backup = Path(backup_path)

        backup.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        backup.write_text(
            self.file_path.read_text(
                encoding="utf-8"
            ),
            encoding="utf-8"
        )

    # --------------------------------------------------
    # Export
    # --------------------------------------------------

    def export_json(
        self,
        export_path: str
    ):

        self.backup(export_path)

    # --------------------------------------------------
    # Import
    # --------------------------------------------------

    def import_json(
        self,
        import_path: str
    ):

        source = Path(import_path)

        if not source.exists():

            raise FileNotFoundError(
                import_path
            )

        self.file_path.write_text(
            source.read_text(
                encoding="utf-8"
            ),
            encoding="utf-8"
        )

    # --------------------------------------------------
    # File Size
    # --------------------------------------------------

    def file_size(self):

        if not self.exists():

            return 0

        return self.file_path.stat().st_size

    # --------------------------------------------------
    # Representation
    # --------------------------------------------------

    def __repr__(self):

        return (
            f"<AutomationStorage("
            f"path='{self.file_path}'"
            f")>"
        )
