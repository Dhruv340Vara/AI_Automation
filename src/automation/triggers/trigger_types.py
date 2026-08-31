from __future__ import annotations

from enum import Enum


class TriggerType(Enum):

    TIME = "time"

    INTERVAL = "interval"

    EVENT = "event"

    COMMAND = "command"

    FILE = "file"

    WEBHOOK = "webhook"

    API = "api"

    MANUAL = "manual"
