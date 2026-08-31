from automation.ai.memory_engine import (
    MemoryEngine,
)

memory = MemoryEngine()

memory.clear()

print(memory)

print()

memory.set(
    "user_name",
    "Dhruv",
)

memory.set(
    "language",
    "Gujarati",
)

memory.set(
    "editor",
    "VS Code",
)

print("User:")

print(
    memory.get(
        "user_name"
    )
)

print()

print("Exists:")

print(
    memory.exists(
        "language"
    )
)

print()

print("Keys:")

print(
    memory.keys()
)

print()

print("Values:")

print(
    memory.values()
)

print()

print("Search:")

print(
    memory.search(
        "vs"
    )
)

print()

memory.remove(
    "editor"
)

print("After Remove:")

print(
    memory.keys()
)

memory.clear()

print()

print("After Clear:")

print(
    memory.keys()
)
