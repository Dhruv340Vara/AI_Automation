from __future__ import annotations

from automation.events.event import Event
from automation.events.event_types import EventType


class WebhookEventFactory:
    """
    Factory for creating webhook events.
    """

    @staticmethod
    def request(
        endpoint: str,
        method: str,
        headers: dict | None = None,
        body: dict | None = None,
        remote_addr: str | None = None,
    ) -> Event:

        return Event(
            event_type=EventType.WEBHOOK,
            source="webhook",
            payload={
                "endpoint": endpoint,
                "method": method.upper(),
                "headers": headers or {},
                "body": body or {},
                "remote_addr": remote_addr,
            },
        )

    @staticmethod
    def github_push(
        repository: str,
        branch: str,
        commit: str,
        sender: str,
        payload: dict | None = None,
    ) -> Event:

        return Event(
            event_type=EventType.WEBHOOK,
            source="github",
            payload={
                "provider": "github",
                "repository": repository,
                "branch": branch,
                "commit": commit,
                "sender": sender,
                "data": payload or {},
            },
        )

    @staticmethod
    def custom(
        provider: str,
        payload: dict,
    ) -> Event:

        return Event(
            event_type=EventType.WEBHOOK,
            source=provider,
            payload={
                "provider": provider,
                "data": payload,
            },
        )
