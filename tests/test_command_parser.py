from automation.commands.command_parser import (
    CommandParser,
)

parser = CommandParser()

print(parser)

print()

# ---------------------------- #

text = "   Open    Firefox   "

print("Original:")
print(text)

print()

parsed = parser.parse(text)

print("Parsed:")
print(parsed)

print()

tokens = parser.tokenize(text)

print("Tokens:")
print(tokens)
