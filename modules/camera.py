import subprocess
import os
from datetime import datetime


SAVE_DIR = "/storage/emulated/0/AI_Automation"

os.makedirs(SAVE_DIR, exist_ok=True)


def capture_photo(camera="0"):
    try:

        filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"

        filepath = os.path.join(SAVE_DIR, filename)

        result = subprocess.run(
            [
                "termux-camera-photo",
                "-c",
                camera,
                filepath
            ],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return {
                "success": False,
                "error": result.stderr.strip()
            }

        return {
            "success": True,
            "file": filepath
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
