from automation.triggers.webhook_trigger import (
    WebhookTrigger,
)

trigger = WebhookTrigger(
    name="GitHub Push",
    endpoint="/github",
    methods=["POST"],
    secret="my_secret",
)

print(trigger)

print(trigger.endpoint)

print(trigger.methods)

print(trigger.accepts_method("POST"))

print(trigger.accepts_method("GET"))

print(trigger.validate_secret("my_secret"))

print(trigger.validate_secret("wrong_secret"))
