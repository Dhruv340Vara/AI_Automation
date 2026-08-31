import subprocess
import json


def get_battery_info():
    try:
        result = subprocess.run(
            ["termux-battery-status"],
            capture_output=True,
            text=True
        )

        return json.loads(result.stdout)

    except Exception as e:
        return {
            "error": str(e)
        }
