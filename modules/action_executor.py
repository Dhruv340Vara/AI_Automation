import requests

class ActionExecutor:
    def __init__(self,base_url="http://127.0.0.1:5000"):
        self.base_url=base_url

    def execute(self,intent):
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
