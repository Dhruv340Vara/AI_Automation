from __future__ import annotations

import json
from pathlib import Path

from automation.triggers.trigger import Trigger


class TriggerStorage:

    def __init__(

        self,

        file_path: str = "data/triggers.json",

    ):

        self.file_path = Path(file_path)

        self.file_path.parent.mkdir(

            parents=True,

            exist_ok=True,

        )

    def save(

        self,

        triggers,

    ):

        data = [

            trigger.to_dict()

            for trigger in triggers

        ]

        with self.file_path.open(

            "w",

            encoding="utf-8",

        ) as f:

            json.dump(

                data,

                f,

                indent=4,

            )

        return True

    def load(self):

        if not self.file_path.exists():

            return []

        with self.file_path.open(

            "r",

            encoding="utf-8",

        ) as f:

            data = json.load(f)

        return [

            Trigger.from_dict(item)

            for item in data

        ]
