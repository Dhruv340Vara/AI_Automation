"""
voice_output.py

Convert text to speech (offline).
"""

import pyttsx3


class VoiceOutput:

    def __init__(self):

        self.engine = pyttsx3.init()

        # speed control
        self.engine.setProperty("rate", 170)

        # volume (0.0 to 1.0)
        self.engine.setProperty("volume", 1.0)

    # ---------------------------- #

    def speak(self, text: str):

        if not text:
            return

        print("🔊 Assistant:", text)

        self.engine.say(text)
        self.engine.runAndWait()

    # ---------------------------- #

    def __repr__(self):

        return "<VoiceOutput>"
