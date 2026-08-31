from automation.ai.memory_store import (
    MemoryStore,
)

store = MemoryStore()

print(store)

print()

print("Exists:")
print(store.exists())

print()

data = {

    "user_name": "Dhruv",

    "language": "Gujarati",

    "editor": "VS Code",

}

store.save(data)

loaded = store.load()

print("Loaded:")

print(loaded)

print()

store.clear()

print("After Clear:")

print(store.load())
