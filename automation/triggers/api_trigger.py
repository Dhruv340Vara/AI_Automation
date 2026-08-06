from __future__ import annotations

from automation.triggers.trigger import Trigger
from automation.triggers.trigger_types import (
    TriggerType,
)


class APITrigger(Trigger):
    """
    Trigger for polling REST APIs.
    """

    def __init__(
        self,
        name: str,
        url: str,
        method: str = "GET",
        interval: int = 60,
        headers: dict | None = None,
        params: dict | None = None,
        body: dict | None = None,
        authentication: dict | None = None,
        timeout: int = 30,
    ):

        metadata = {
            "url": url,
            "method": method.upper(),
            "interval": interval,
            "headers": headers or {},
            "params": params or {},
            "body": body or {},
            "authentication": authentication or {},
            "timeout": timeout,
        }

        super().__init__(
            trigger_type=TriggerType.API,
            name=name,
            metadata=metadata,
        )

    # -------------------------------- #

    @property
    def url(self):

        return self.metadata["url"]

    @property
    def method(self):

        return self.metadata["method"]

    @property
    def interval(self):

        return self.metadata["interval"]

    @property
    def headers(self):

        return self.metadata["headers"]

    @property
    def params(self):

        return self.metadata["params"]

    @property
    def body(self):

        return self.metadata["body"]

    @property
    def authentication(self):

        return self.metadata["authentication"]

    @property
    def timeout(self):

        return self.metadata["timeout"]

    # -------------------------------- #

    def is_get(self):

        return self.method == "GET"

    def is_post(self):

        return self.method == "POST"

    # -------------------------------- #

    def __repr__(self):

        return (
            "<APITrigger "
            f"{self.name} "
            f"{self.method} "
            f"{self.url}>"
        )
