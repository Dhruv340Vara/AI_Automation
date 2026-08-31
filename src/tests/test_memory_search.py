from automation.ai.memory_search import (
    MemorySearch,
)

search = MemorySearch()

memory = {

    "user_name": "Dhruv",

    "language": "Gujarati",

    "editor": "VS Code",

    "theme": "Dark",

}

print(search)

print()

print(search.find(
    memory,
    "language",
))

print()

print(search.exists(
    memory,
    "theme",
))

print()

print(search.keys(
    memory,
))

print()

print(search.values(
    memory,
))

print()

print(search.search(
    memory,
    "vs",
))
