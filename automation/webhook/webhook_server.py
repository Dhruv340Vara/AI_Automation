from __future__ import annotations

from automation.webhook.webhook_request import (
    WebhookRequest,
)

from automation.events.webhook_event import (
    WebhookEventFactory,
)


class WebhookServer:
    """
    Lightweight webhook server abstraction.

    Framework independent.
    Flask/FastAPI integration will
    come later.
    """

    def __init__(self):

        self._routes = {}

    # -------------------------------- #

    def register(
        self,
        trigger,
    ):

        self._routes[
            trigger.endpoint
        ] = trigger

    # -------------------------------- #

    def unregister(
        self,
        endpoint: str,
    ):

        self._routes.pop(
            endpoint,
            None,
        )

    # -------------------------------- #

    def has_route(
        self,
        endpoint: str,
    ):

        return (
            endpoint
            in self._routes
        )

    # -------------------------------- #

    def handle(
        self,
        request: WebhookRequest,
    ):

        trigger = self._routes.get(
            request.endpoint
        )

        if trigger is None:
            return None

        if not trigger.accepts_method(
            request.method
        ):
            return None

        secret = request.header(
            "X-Webhook-Secret"
        )

        if not trigger.validate_secret(
            secret
        ):
            return None

        return (
            WebhookEventFactory.request(
                endpoint=request.endpoint,
                method=request.method,
                headers=request.headers,
                body=request.body,
                remote_addr=request.remote_addr,
            )
        )

    # -------------------------------- #

    def route_count(self):

        return len(
            self._routes
        )

    # -------------------------------- #

    def __repr__(self):

        return (
            "<WebhookServer "
            f"routes={self.route_count()}>"
        )
