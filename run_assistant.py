from voice_input import listen
from command_parser import parse_command
from api_client import execute_action

print("🤖 Assistant Started...")

while True:
    text = listen()

    if not text:
        continue

    command = parse_command(text)
    execute_action(command)
