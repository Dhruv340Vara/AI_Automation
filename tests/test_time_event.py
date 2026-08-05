from automation.events import TimeEventFactory

from datetime import datetime

event = TimeEventFactory.once(
    datetime.now()
)

print(event)

print(event.payload)
