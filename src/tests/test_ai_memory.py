from automation.ai.ai_brain import (
    AIBrain,
)

brain = AIBrain()

brain.clear_memory()

print(brain)

print()

brain.remember(

    "user_name",

    "Dhruv",

)

brain.remember(

    "language",

    "Gujarati",

)

print(

    brain.recall(

        "user_name"

    )

)

print()

print(

    brain.search_memory(

        "guj"

    )

)

print()

brain.forget(

    "language"

)

print(

    brain.search_memory(

        "language"

    )

)

brain.clear_memory()

print()

print(

    brain.search_memory(

        ""

    )

)