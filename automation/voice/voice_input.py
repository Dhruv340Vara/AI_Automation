"""
voice_input.py

Convert speech to text using microphone.
"""

import speech_recognition as sr


class VoiceInput:

    def __init__(self):

        self.recognizer = sr.Recognizer()

    # ---------------------------- #

    def listen(self) -> str | None:

        try:

            with sr.Microphone() as source:

                print("🎤 Listening...")

                # background noise adjust
                self.recognizer.adjust_for_ambient_noise(source, duration=1)

                audio = self.recognizer.listen(source)

            print("🧠 Recognizing...")

            text = self.recognizer.recognize_google(audio)

            print("You said:", text)

            return text.lower()

        # ---------------------------- #

        except sr.UnknownValueError:

            print("❌ Could not understand audio")
            return None

        except sr.RequestError as e:

            print("❌ API error:", e)
            return None

        except Exception as e:

            print("❌ Error:", e)
            return None

    # ---------------------------- #

    def __repr__(self):

        return "<VoiceInput>"
