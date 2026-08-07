import requests


class HttpClient:

    def __init__(self, base_url="http://127.0.0.1:5000"):
        self.base_url = base_url

    def post(self, endpoint, data=None):

        url = f"{self.base_url}/{endpoint}"

        try:
            response = requests.post(url, json=data)
            return response.json()

        except Exception as e:
            print("HTTP Error:", e)
            return None
