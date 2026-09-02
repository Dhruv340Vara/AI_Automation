from automation.ai.ai_brain import AIBrain
from automation.ai.llm.ollama_adapter import OllamaAdapter


llm = OllamaAdapter(
    model="qwen2.5:7b"
)

brain = AIBrain(
    llm=llm,
    max_history=4,
)


messages = [
    "My name is Dhruv.",
    "I am working on an AI automation project.",
    "The project uses a local LLM.",
    "The LLM is running with Ollama.",
    "What is my name?",
    "What kind of project am I working on?",
]


for message in messages:

    print("\n" + "=" * 60)
    print("USER:", message)

    response = brain.ask(message)

    print("ASSISTANT:", response.content)


print("\n" + "=" * 60)
print("TOTAL STORED HISTORY:", len(brain.history()))

print("\nFULL AIContext HISTORY:")

for i, message in enumerate(brain.history(), start=1):

    print(
        f"{i}. "
        f"{message.role.value}: "
        f"{message.content}"
    )


print("\n" + "=" * 60)
print("LLM CONTEXT:")

llm_context = brain._build_llm_context()

for i, message in enumerate(
    llm_context["conversation"],
    start=1,
):

    print(
        f"{i}. "
        f"{message['role']}: "
        f"{message['content']}"
    )