from automation.ai.ai_brain import AIBrain
from automation.ai.llm.ollama_adapter import OllamaAdapter


llm = OllamaAdapter(
    model="qwen2.5:7b"
)

brain = AIBrain(llm=llm)

print("LLM available:", brain.llm_available())


response = brain.ask(
    "My name is Dhruv."
)

print("\nUser: My name is Dhruv.")
print("Assistant:", response.content)


response = brain.ask(
    "What is my name?"
)

print("\nUser: What is my name?")
print("Assistant:", response.content)


print("\nHistory:")

for message in brain.history():
    print(
        f"{message.role.value}: "
        f"{message.content}"
    )