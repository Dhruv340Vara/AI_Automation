from automation.triggers.webhook_trigger import (
    WebhookTrigger,
)

from automation.webhook import (
    WebhookRequest,
    WebhookServer,
)

server = WebhookServer()

trigger = WebhookTrigger(

    name="GitHub",

    endpoint="/github",

    methods=["POST"],

    secret="12345",

)

server.register(
    trigger
)

request = WebhookRequest(

    endpoint="/github",

    method="POST",

    headers={
        "X-Webhook-Secret": "12345",
    },

    body={
        "event": "push",
    },

    remote_addr="127.0.0.1",

)

event = server.handle(
    request
)

print(server)

print(event)

print(event.payload)
