from automation.ai.memory_engine import (
    MemoryEngine,
)

print("=" * 60)
print("             MEMORY TEST SUITE")
print("=" * 60)

memory = MemoryEngine()

print()
print("Clearing Memory...")

memory.clear()

assert memory.keys() == []

print("PASS")

print()
print("Saving Memory...")

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

assert memory.exists(
    "user_name"
)

assert memory.exists(
    "language"
)

assert memory.exists(
    "editor"
)

print("PASS")

print()
print("Reading Memory...")

assert (
    memory.get(
        "user_name"
    )
    == "Dhruv"
)

assert (
    memory.get(
        "language"
    )
    == "Gujarati"
)

assert (
    memory.get(
        "editor"
    )
    == "VS Code"
)

print("PASS")

print()
print("Searching Memory...")

result = memory.search(
    "vs"
)

assert (
    result["editor"]
    == "VS Code"
)

print("PASS")

print()
print("Removing Memory...")

assert memory.remove(
    "editor"
)

assert (
    not memory.exists(
        "editor"
    )
)

print("PASS")

print()
print("Listing Keys...")

keys = memory.keys()

assert (
    "user_name"
    in keys
)

assert (
    "language"
    in keys
)

print(keys)

print("PASS")

print()
print("Listing Values...")

values = memory.values()

assert (
    "Dhruv"
    in values
)

assert (
    "Gujarati"
    in values
)

print(values)

print("PASS")

print()
print("Clearing Memory...")

memory.clear()

assert memory.keys() == []

print("PASS")

print()

print("=" * 60)
print("ALL MEMORY TESTS PASSED")
print("=" * 60)
