from __future__ import annotations
import time
import threading
from datetime import datetime
from typing import Optional

class Timer:

    def __init__(self):
        self._stop_event = threading.Event()

    @staticmethod
    def now() -> datetime:
        return datetime.now()

    @staticmethod
    def timestamp() -> float:
        return time.time()

    @staticmethod
    def sleep(seconds: float) -> None:
        if seconds <= 0:
            return
        time.sleep(seconds)

    @staticmethod
    def elapsed(start: float) -> float:
        return time.time() - start

    @staticmethod
    def wait_until(target: datetime) -> float:
        remaining = (target - datetime.now()).total_seconds()
        return max(0.0, remaining)

    @staticmethod
    def is_due(target: datetime) -> bool:
        return datetime.now() >= target

    @staticmethod
    def format(dt: Optional[datetime]) -> str:
        if dt is None:
            return "None"
        return dt.strftime("%Y-%m-%d %H:%M:%S")

    def wait(self, seconds: float) -> bool:
        interrupted = self._stop_event.wait(seconds)
        return not interrupted

    def stop(self):
        self._stop_event.set()

    def reset(self):
        self._stop_event.clear()

    def is_stopped(self):
        return self._stop_event.is_set()
