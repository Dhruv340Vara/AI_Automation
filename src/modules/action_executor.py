from modules.apps import AppManager
import requests

class ActionExecutor:
    def __init__(self,base_url="http://127.0.0.1:5000"):
        self.base_url=base_url
        self.apps = AppManager()

    def execute(self, intent, data=None):
        if data is None:
            data = {}

        if intent=="OPEN_CAMERA":
            return self._open_camera()

        if intent=="OPEN_GALLERY":
            return{
                "success":False,
                "message":"Gallery action is not implemented yet."
            }

        if intent=="TORCH_ON":
            return self._torch("on")

        if intent=="TORCH_OFF":
            return self._torch("off")

        if intent == "OPEN_APP":
            return self.apps.open_app(
                data.get("app")
            )

        return{
            "success":False,
            "message":"Unknown intent."
        }

    def _open_camera(self):
        return self._post(
            "/camera",
            {
                "camera":"0"
            }
        )

    def _torch(self,action):
        return self._post(
            "/torch",
            {
                "action":action
            }
        )

    def _post(self,endpoint,data):
        try:
            response=requests.post(
                self.base_url+endpoint,
                json=data,
                timeout=15
            )
            return response.json()
        except Exception as e:
            return{
                "success":False,
                "message":str(e)
            }
