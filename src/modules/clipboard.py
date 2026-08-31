import subprocess


def get_clipboard():
    try:
        result = subprocess.run(
            ["termux-clipboard-get"],
            capture_output=True,
            text=True
        )

        return {
            "text": result.stdout.strip()
        }

    except Exception as e:
        return {
            "error": str(e)
        }


def set_clipboard(text):
    try:
        subprocess.run(
            ["termux-clipboard-set", text],
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
