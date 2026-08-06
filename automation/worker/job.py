from __future__ import annotations
import uuid
from typing import Callable, Any
from datetime import datetime, timedelta

class Job:

    def __init__(self,target: Callable,*args,**kwargs):
        self.job_id = str(uuid.uuid4())
        self.target = target
        self.args = args
        self.max_retries = kwargs.pop("max_retries",0,)
        self.retry_delay = kwargs.pop("retry_delay",0,)
        self.kwargs = kwargs
        self.created_at = datetime.now()
        self.attempts = 0
        self.result = None
        self.error = None
        self.next_retry_at = None

    def execute(self):
        self.attempts += 1
        try:
            if callable(self.target):
                self.result = self.target(*self.args,**self.kwargs,)
            else:
                self.result = self.target
            self.error = None
            return True
        except Exception as exc:
            self.error = exc
            return False

    def __repr__(self):
        return f"<Job {self.job_id[:8]}>"
    
    def should_retry(self):
        if self.attempts > self.max_retries:
            return False
        if self.next_retry_at is None:
            return True
        return datetime.now() >= self.next_retry_at

    def schedule_retry(self):
        self.next_retry_at = (
            datetime.now()
            + timedelta(
                seconds=self.retry_delay
            )
        )
