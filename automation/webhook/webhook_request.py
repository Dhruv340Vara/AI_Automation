from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class WebhookRequest:
    """
    Represents an incoming webhook request.
    """

    endpoint: str

    method: str

    headers: dict = field(
        default_factory=dict
    )

    body: dict = field(
        default_factory=dict
    )

    remote_addr: str | None = None

    def header(
        self,
        name: str,
        default=None,
    ):
        return self.headers.get(
            name,
            default,
        )

    def __repr__(self):

        return (
            "<WebhookRequest "
            f"{self.method} "
            f"{self.endpoint}>"
        )
