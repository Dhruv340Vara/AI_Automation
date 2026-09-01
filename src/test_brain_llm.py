import time

from automation.ai.ai_brain import AIBrain
from automation.ai.llm.ollama_adapter import OllamaAdapter


llm = OllamaAdapter(
    model="qwen2.5:7b"
)

brain = AIBrain(llm=llm)

print(brain)

print("LLM available:", brain.llm_available())

start = time.time()

response = brain.ask("Hello, introduce yourself.")

elapsed = time.time() - start

print("Time:", round(elapsed, 2), "seconds")

print("Success:", response.success)

print("Response:", response.content)