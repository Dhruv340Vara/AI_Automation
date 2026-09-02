from automation.ai.memory_engine import MemoryEngine


memory = MemoryEngine()

print("\n=== Memory Ranking Test ===")


memories = [
    ("My name is Dhruv.", "user", 0.95),
    ("I like Python.", "user", 0.85),
    ("ok", "user", 0.05),
    ("thanks", "user", 0.05),
    ("I am building an AI assistant.", "user", 0.95),
]

for content, role, importance in memories:
    memory.remember_conversation(
        role=role,
        content=content,
        importance=importance,
    )


print("\n1. Search: name")

results = memory.search_conversation(
    "What is my name?",
    limit=5,
)

for result in results:
    print(
        f"[importance={result['importance']:.2f}] "
        f"{result['content']}"
    )

assert results
assert results[0]["content"] == "My name is Dhruv."

print("PASS")


print("\n2. Search: Python")

results = memory.search_conversation(
    "Which programming language do I like?",
    limit=5,
)

for result in results:
    print(
        f"[importance={result['importance']:.2f}] "
        f"{result['content']}"
    )

assert results
assert results[0]["content"] == "I like Python."

print("PASS")


print("\n3. Search: AI assistant")

results = memory.search_conversation(
    "What project am I building?",
    limit=5,
)

for result in results:
    print(
        f"[importance={result['importance']:.2f}] "
        f"{result['content']}"
    )

assert results
assert results[0]["content"] == "I am building an AI assistant."

print("PASS")


print("\n======================================")
print("MEMORY RANKING TEST PASSED")
print("======================================")
