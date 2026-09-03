"""
voice_input.py

Convert speech to text using microphone.
"""

import speech_recognition as sr


class VoiceInput:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self) -> str | None:
        try:
            # Always resolve the current system default microphone.
            # Do not cache a PyAudio device index because device
            # enumeration can change after TTS/ALSA activity.
            with sr.Microphone() as source:
                print("🎤 Listening...")
                self.recognizer.adjust_for_ambient_noise(
                    source,
                    duration=1
                )
                print("🗣️ Speak now...")
                audio = self.recognizer.listen(source)

            print("🧠 Recognizing...")
            text = self.recognizer.recognize_google(audio)

            print("You said:", text)
            return text.lower()

        except sr.UnknownValueError:
            print("❌ Could not understand audio")
            return None

        except sr.RequestError as error:
            print("❌ API error:", error)
            return None

        except Exception as error:
            print("❌ Error:", error)
            return None

    def __repr__(self):
        return "<VoiceInput>"