import subprocess
import json


def get_wifi_info():
    try:
        result = subprocess.run(
            ["termux-wifi-connectioninfo"],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return {
                "connected": False,
                "error": result.stderr.strip()
            }

        data = json.loads(result.stdout)

        return {
            "connected": True,
            "ssid": data.get("ssid"),
            "bssid": data.get("bssid"),
            "ip": data.get("ip"),
            "frequency": data.get("frequency"),
            "link_speed": data.get("link_speed_mbps"),
            "rssi": data.get("rssi"),
            "network_id": data.get("network_id")
        }

    except Exception as e:
        return {
            "connected": False,
            "error": str(e)
        }
