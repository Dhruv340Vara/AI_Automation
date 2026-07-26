import subprocess


def vibrate(duration=500):
    try:
        subprocess.run(
            ["termux-vibrate", "-d", str(duration)],
            capture_output=True,
            text=True
        )

        return {
            "status": "success",
            "duration": duration
        }

    except Exception as e:
        return {
            "error": str(e)
        }
