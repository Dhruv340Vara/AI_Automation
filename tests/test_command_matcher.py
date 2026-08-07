from automation.commands.command_parser import (
    CommandParser,
)

from automation.commands.command_matcher import (
    CommandMatcher,
)


parser = CommandParser()
matcher = CommandMatcher()

print(matcher)

print()

commands = [
    "Open Firefox",
    "Run pwd",
    "Create folder Test",
    "Delete file demo.txt",
    "Copy folder A B",
    "Move file A B",
    "Unknown command",
]

for cmd in commands:

    parsed = parser.parse(cmd)
    tokens = parser.tokenize(cmd)

    action = matcher.match(tokens)

    print(f"{cmd} → {action}")
