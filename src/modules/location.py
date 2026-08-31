import subprocess
import json


def get_location():
    try:
        result = subprocess.run(
            ["termux-location"],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return {
                "success": False,
                "error": result.stderr.strip()
            }

        output = result.stdout.strip()

        if not output:
            return {
                "success": False,
                "error": "No location data returned"
            }

        data = json.loads(output)

        return {
            "success": True,
            "provider": data.get("provider"),
            "latitude": data.get("latitude"),
            "longitude": data.get("longitude"),
            "altitude": data.get("altitude"),
            "accuracy": data.get("accuracy"),
            "bearing": data.get("bearing"),
            "speed": data.get("speed")
        }

    except json.JSONDecodeError:
        return {
            "success": False,
            "error": "Invalid JSON received",
            "raw_output": result.stdout
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
