from automation.assistant.command_matcher import (
    CommandMatcher,
)

matcher = CommandMatcher()

matcher.register(

    "call",

    "call",

    "dial",

    "phone",

)

matcher.register(

    "torch",

    "torch",

    "flashlight",

    "flash",

)

matcher.register(

    "wifi",

    "wifi",

    "internet",

)

print(matcher)

print()

print(

    matcher.match(

        "Call Mummy"

    )

)

print(

    matcher.match(

        "Turn on flashlight"

    )

)

print(

    matcher.match(

        "Disable WiFi"

    )

)

print(

    matcher.match(

        "Open Chrome"

    )

)

print()

print(

    matcher.rules()

)
