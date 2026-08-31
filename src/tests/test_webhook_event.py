from automation.events.webhook_event import (
    WebhookEventFactory,
)

event = WebhookEventFactory.request(
    endpoint="/github",
    method="POST",
    headers={
        "Content-Type": "application/json",
    },
    body={
        "action": "push",
    },
    remote_addr="127.0.0.1",
)

print(event)

print(event.event_type.value)

print(event.payload)

print("-" * 50)

github = WebhookEventFactory.github_push(
    repository="AI_Automation",
    branch="main",
    commit="abc123",
    sender="Dhruv",
)

print(github.payload)

print("-" * 50)

custom = WebhookEventFactory.custom(
    provider="TradingView",
    payload={
        "symbol": "NIFTY",
        "signal": "BUY",
    },
)

print(custom.payload)
