from automation.voice.voice_input import VoiceInput
from automation.voice.voice_output import VoiceOutput
from modules.command_parser import CommandParser
import requests

API_URL = "http://127.0.0.1:5000/execute"

voice_in = VoiceInput()
voice_out = VoiceOutput()
parser = CommandParser()


def run_assistant():
    voice_out.speak("Assistant started")

    while True:

        # 🎤 Listen
        text = voice_in.listen()

        if not text:
            continue

        # 🧠 Parse
        result = parser.parse(text)

        print("DEBUG:", result)

        if not result["success"]:
            voice_out.speak("Sorry, I did not understand")
            continue

        # 🔥 Convert intent → action
        action = result["intent"].lower()

        payload = result.get("data", {})

        try:
            # 🌐 Call backend
            res = requests.post(API_URL, json={
                "action": action,
                "data": payload
            })

            data = res.json()

            if data.get("success"):
                msg = data.get("message", "Done")
                voice_out.speak(msg)
            else:
                voice_out.speak("Error occurred")

        except Exception as e:
            print("API Error:", e)
            voice_out.speak("Server not reachable")


if __name__ == "__main__":
    run_assistant()