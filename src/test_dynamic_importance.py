from automation.ai.memory_engine import MemoryEngine


memory = MemoryEngine("memory/test_importance.json")

print("\n=== Dynamic Memory Importance Test ===")

tests = [
    ("My name is Dhruv.", "user"),
    ("I prefer Python over PHP.", "user"),
    ("I am building an AI assistant.", "user"),
    ("Remember that I use Ollama.", "user"),
    ("Let's discuss AI.", "user"),
    ("ok", "user"),
    ("thanks", "user"),
    ("Hello!", "user"),
    ("Hello Dhruv! Nice to meet you.", "assistant"),
]

for content, role in tests:
    importance = memory.calculate_importance(
        content=content,
        role=role,
    )

    print(
        f"[{importance:.2f}] "
        f"{role}: {content}"
    )

print("\nPASS")

