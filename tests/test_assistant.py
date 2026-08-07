from automation.core.assistant import Assistant


assistant = Assistant()

commands = [
    "Open Firefox",
    "Run pwd",
    "Create folder test123",
]

for cmd in commands:
    assistant.handle(cmd)
