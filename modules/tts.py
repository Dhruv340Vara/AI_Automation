import subprocess


def speak(text):

    try:

        subprocess.run(
            ["termux-tts-speak", text],
            capture_output=True,
            text=True
        )

        return {
            "status": "success",
            "text": text
        }

    except Exception as e:

        return {
            "error": str(e)
        }
