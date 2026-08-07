import speech_recognition as sr

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("🗣️ You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("❌ Could not understand")
        return ""
    except sr.RequestError:
        print("❌ API error")
        return ""

