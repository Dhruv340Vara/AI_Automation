from __future__ import annotations

from automation.triggers.trigger import Trigger
from automation.triggers.trigger_types import (
    TriggerType,
)


class WebhookTrigger(Trigger):
    """
    Trigger for HTTP webhook requests.
    """

    def __init__(
        self,
        name: str,
        endpoint: str,
        methods: list[str] | None = None,
        secret: str | None = None,
        headers: dict | None = None,
    ):

        metadata = {
            "endpoint": endpoint,
            "methods": methods or ["POST"],
            "secret": secret,
            "headers": headers or {},
        }

        super().__init__(
            trigger_type=TriggerType.WEBHOOK,
            name=name,
            metadata=metadata,
        )

    # -------------------------------- #

    @property
    def endpoint(self) -> str:

        return self.metadata["endpoint"]

    @property
    def methods(self) -> list[str]:

        return self.metadata["methods"]

    @property
    def secret(self) -> str | None:

        return self.metadata["secret"]

    @property
    def headers(self) -> dict:

        return self.metadata["headers"]

    # -------------------------------- #

    def accepts_method(
        self,
        method: str,
    ) -> bool:

        return (
            method.upper()
            in self.methods
        )

    # -------------------------------- #

    def validate_secret(
        self,
        secret: str | None,
    ) -> bool:

        if self.secret is None:
            return True

        return secret == self.secret

    # -------------------------------- #

    def __repr__(self):

        return (
            "<WebhookTrigger "
            f"{self.name} "
            f"endpoint={self.endpoint}>"
        )
