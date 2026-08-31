import requests

BASE_URL = "http://127.0.0.1:5000"

def execute_action(command):
    action = command["action"]

    try:
        if action == "camera":
            requests.get(f"{BASE_URL}/camera/open")
            print("📸 Camera opened")

        elif action == "torch_on":
            requests.get(f"{BASE_URL}/torch/on")
            print("🔦 Torch ON")

        elif action == "torch_off":
            requests.get(f"{BASE_URL}/torch/off")
            print("🔦 Torch OFF")

        elif action == "battery":
            res = requests.get(f"{BASE_URL}/battery")
            print("🔋 Battery:", res.json())

        elif action == "wifi_on":
            requests.get(f"{BASE_URL}/wifi/on")
            print("📶 WiFi ON")

        elif action == "wifi_off":
            requests.get(f"{BASE_URL}/wifi/off")
            print("📶 WiFi OFF")

        else:
            print("❓ Unknown command")

    except Exception as e:
        print("❌ Error:", e)
