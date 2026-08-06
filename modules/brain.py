from modules.command_parser import CommandParser
from modules.context import ContextEngine
from modules.planner import Planner
from modules.executor import Executor
import time

class Brain:
    def __init__(self):
        self.parser = CommandParser()
        self.context = ContextEngine()
        self.planner = Planner()
        self.executor = Executor()
        self.total_requests = 0
        self.success_requests = 0
        self.failed_requests = 0

    def process(self, message):
        try:
            start_time = time.time()
            self.total_requests += 1
            parsed = self.parser.parse(message)
            context = self.context.get_context(message)
            if isinstance(parsed, dict):
                if "intent" in parsed:
                    context["intent"] = parsed["intent"]
                if "entities" in parsed:
                    context["entities"] = parsed["entities"]
            plan = self.planner.create_plan(context)
            result = self.executor.execute(plan)
            execution_time = round(
                time.time() - start_time,
                3
            )
            try:
                self.context.remember_conversation(
                    "user",
                    message
                )
                self.context.remember_conversation(
                    "assistant",
                    str(result)
                )
            except:
                pass
            try:
                self.context.remember_action(
                    plan["action"]
                )
            except:
                pass
            self.success_requests += 1
            return {
                "success": True,
                "message": message,
                "execution_time": execution_time,
                "context": context,
                "plan": plan,
                "result": result
            }
        except Exception as e:
            self.failed_requests += 1
            return {
                "success": False,
                "error": str(e)
            }

    def status(self):
        return {
            "parser": True,
            "context": True,
            "planner": True,
            "executor": True,
            "pipeline": "ready"
        }

    def statistics(self):
        success_rate = 0
        if self.total_requests > 0:
            success_rate = round(
                (self.success_requests /
                self.total_requests) * 100,
                2
            )
        return {
            "total_requests": self.total_requests,
            "successful_requests": self.success_requests,
            "failed_requests": self.failed_requests,
            "success_rate": success_rate
        }

    def pipeline(self):
        return [
            "Parser",
            "Context",
            "Planner",
            "Executor"
        ]

    def reset_statistics(self):
        self.total_requests = 0
        self.success_requests = 0
        self.failed_requests = 0
