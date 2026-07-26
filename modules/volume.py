import subprocess
import json


def get_volume():
    try:
        result = subprocess.run(
            ["termux-volume"],
            capture_output=True,
            text=True
        )

        return json.loads(result.stdout)

    except Exception as e:
        return {
            "error": str(e)
        }


def set_volume(stream, volume):
    try:
        subprocess.run(
            ["termux-volume", stream, str(volume)],
            capture_output=True,
            text=True
        )

        return {
            "status": "success",
            "stream": stream,
            "volume": volume
        }

    except Exception as e:
        return {
            "error": str(e)
        }
