from __future__ import annotations

import uuid
from datetime import datetime
from typing import Callable, Any


class Job:

    def __init__(
        self,
        target: Callable,
        *args,
        **kwargs
    ):

        self.job_id = str(uuid.uuid4())

        self.target = target

        self.args = args

        self.kwargs = kwargs

        self.created_at = datetime.now()

    def execute(self):

        return self.target(
            *self.args,
            **self.kwargs
        )

    def __repr__(self):

        return f"<Job {self.job_id[:8]}>"
