from modules.action_executor import ActionExecutor
from modules.command_parser import CommandParser

class AIEngine:
    def __init__(self):
        self.parser=CommandParser()
        self.executor=ActionExecutor()

    def process(self,command:str)->dict:
        if command is None:
            return self._error_response("Command is missing.")

        command=command.strip()

        if len(command)==0:
            return self._error_response("Command is empty.")

        try:
            result=self.parser.parse(command)

            if not isinstance(result,dict):
                return self._error_response("Invalid parser response.")

            if result.get("success"):
                action = self.executor.execute(
                    result["intent"],
                    result.get("data", {})
                )

            if isinstance(action,dict):
                result["data"]=action.get("data",action)

            return{
                "success":result.get("success",False),
                "intent":result.get("intent","UNKNOWN"),
                "message":result.get("message","No response."),
                "data":result.get("data",{})
            }

        except Exception as e:
            return{
                "success":False,
                "intent":"ERROR",
                "message":str(e),
                "data":{}
            }

    def _error_response(self,message:str)->dict:
        return{
            "success":False,
            "intent":"ERROR",
            "message":message,
            "data":{}
        }
