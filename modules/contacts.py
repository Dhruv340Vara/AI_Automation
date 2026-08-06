import subprocess
import json


def get_contacts():
    try:
        result = subprocess.run(
            ["termux-contact-list"],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return {
                "success": False,
                "error": result.stderr.strip()
            }

        contacts = json.loads(result.stdout)

        return {
            "success": True,
            "count": len(contacts),
            "contacts": contacts
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
