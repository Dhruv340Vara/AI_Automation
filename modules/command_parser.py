class CommandParser:
    def __init__(self):
        self.intents={
            "OPEN_CAMERA":["camera","open camera","launch camera","camera kholo"],
            "OPEN_GALLERY":["gallery","open gallery","gallery kholo"],
            "TORCH_ON":["torch on","flash on","light on","turn on torch"],
            "TORCH_OFF":["torch off","flash off","light off","turn off torch"]
        }
    def parse(self,command:str)->dict:
        command=command.lower().strip()
        for intent,keywords in self.intents.items():
            for keyword in keywords:
                if keyword in command:
                    return self._success(intent)
        return self._unknown()
    def _success(self,intent:str)->dict:
        messages={
            "OPEN_CAMERA":"Opening camera...",
            "OPEN_GALLERY":"Opening gallery...",
            "TORCH_ON":"Turning torch ON...",
            "TORCH_OFF":"Turning torch OFF..."
        }
        return{
            "success":True,
            "intent":intent,
            "message":messages.get(intent,"Command executed."),
            "data":{}
        }
    def _unknown(self)->dict:
        return{
            "success":False,
            "intent":"UNKNOWN",
            "message":"Sorry, I didn't understand the command.",
            "data":{}
        }
