from automation.ai.memory_engine import MemoryEngine


memory = MemoryEngine()

tests = [
    ("My name is Dhruv.", "fact"),
    ("I live in India.", "fact"),
    ("I like Python.", "preference"),
    ("I prefer Linux over Windows.", "preference"),
    ("I am building an AI assistant.", "goal"),
    ("My project is an automation system.", "goal"),
    ("Remember that I use Ollama.", "instruction"),
    ("From now on use Python.", "instruction"),
    ("Let's discuss AI.", "conversation"),
    ("Hello!", "conversation"),
]


print("\n=== Memory Classification Test ===\n")

passed = 0

for text, expected in tests:
    result = memory.classify_memory(text)

    status = "PASS" if result == expected else "FAIL"

    print(
        f"[{status}] "
        f"{text} -> {result} "
        f"(expected: {expected})"
    )

    if result == expected:
        passed += 1


print()
print(f"{passed}/{len(tests)} tests passed")

if passed == len(tests):
    print("\n======================================")
    print("MEMORY CLASSIFICATION TEST PASSED")
    print("======================================")
else:
    print("\nSome tests failed.")

