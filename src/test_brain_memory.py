from automation.ai.ai_brain import AIBrain
from automation.ai.llm.ollama_adapter import OllamaAdapter


def main():
    print("\n=== AIBrain Memory Retrieval Test ===\n")

    # Create LLM
    llm = OllamaAdapter(
        model="qwen2.5:7b"
    )

    # Create brain
    brain = AIBrain(
        llm=llm,
        max_history=4,
    )

    # Clean memory before test
    brain.clear_memory()

    # --------------------------------------------------
    # 1. Add memories manually
    # --------------------------------------------------
    print("1. Adding Memories")

    memory1 = brain.memory.remember_conversation(
        role="user",
        content="My name is Dhruv.",
        importance=0.9,
    )

    memory2 = brain.memory.remember_conversation(
        role="user",
        content="I am working on an AI automation project.",
        importance=0.9,
    )

    memory3 = brain.memory.remember_conversation(
        role="user",
        content="I use Qwen 2.5 7B with Ollama.",
        importance=0.8,
    )

    print("Memory 1:", memory1)
    print("Memory 2:", memory2)
    print("Memory 3:", memory3)

    print("PASS\n")

    # --------------------------------------------------
    # 2. Test relevant memory retrieval
    # --------------------------------------------------
    print("2. Relevant Memory Retrieval")

    query = "What is my name?"

    memories = brain._retrieve_relevant_memories(
        query=query,
        limit=5,
    )

    print("Query:", query)
    print("Retrieved memories:")

    for memory in memories:
        print(
            f"- [{memory['role']}] "
            f"{memory['content']}"
        )

    assert any(
        "Dhruv" in memory["content"]
        for memory in memories
    )

    print("PASS\n")

    # --------------------------------------------------
    # 3. Test LLM context
    # --------------------------------------------------
    print("3. LLM Context")

    context = brain._build_llm_context(
        query="What is my name?",
        memory_limit=5,
    )

    print("\nConversation:")
    for message in context["conversation"]:
        print(
            f"{message['role']}: "
            f"{message['content']}"
        )

    print("\nRelevant Memories:")
    for memory in context["memories"]:
        print(
            f"{memory['role']}: "
            f"{memory['content']}"
        )

    assert "conversation" in context
    assert "memories" in context

    assert any(
        "Dhruv" in memory["content"]
        for memory in context["memories"]
    )

    print("\nPASS\n")

    # --------------------------------------------------
    # 4. Ask LLM using retrieved memory
    # --------------------------------------------------
    print("4. Ask LLM")

    query = "What is my name?"

    response = brain.ask(query)

    print("User:", query)

    if response.success:
        print("Assistant:", response.content)
    else:
        print("LLM Error:", response.error)

    assert response.success

    print("PASS\n")

    # --------------------------------------------------
    # 5. Final context
    # --------------------------------------------------
    print("5. Final Brain History")

    for message in brain.history():
        print(
            f"{message.role.value}: "
            f"{message.content}"
        )

    print("\nPASS\n")

    # --------------------------------------------------
    # Cleanup
    # --------------------------------------------------
    brain.clear_memory()

    print("======================================")
    print("ALL AIBRAIN MEMORY TESTS PASSED")
    print("======================================")


if __name__ == "__main__":
    main()

