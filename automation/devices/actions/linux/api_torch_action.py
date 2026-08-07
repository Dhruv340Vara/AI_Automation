from automation.devices.actions.device_action import DeviceAction
from automation.utils.http_client import HttpClient


class ApiTorchAction(DeviceAction):

    def __init__(self):
        super().__init__("torch")
        self.client = HttpClient()

    def perform(self, request):

        state = request.get_parameter("state", "on")

        result = self.client.post(
            "torch",
            {"state": state}
        )

        print("API Response:", result)

        return True

