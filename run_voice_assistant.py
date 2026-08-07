from automation.core.assistant import Assistant
from automation.voice.voice_input import VoiceInput


assistant = Assistant()
voice = VoiceInput()

print("🤖 Voice Assistant Ready (say 'exit')\n")

while True:

    text = voice.listen()

    if not text:
        continue

    if "exit" in text:
        assistant.voice.speak("Goodbye")
        break

    assistant.handle(text)
