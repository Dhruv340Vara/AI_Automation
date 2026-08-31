from automation.commands.command_parser import CommandParser
from automation.commands.command_matcher import CommandMatcher
from automation.commands.command_mapper import CommandMapper


parser = CommandParser()
matcher = CommandMatcher()
mapper = CommandMapper()

commands = [
    "Open Firefox",
    "Run pwd",
    "Create folder Test",
    "Delete file demo.txt",
    "Move file A B",
]

for cmd in commands:

    tokens = parser.tokenize(cmd)
    action = matcher.match(tokens)

    request = mapper.map(action, tokens)

    print(cmd)
    print(request)
    print(request.parameters if request else None)
    print()
