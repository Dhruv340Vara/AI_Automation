class Planner:
    def __init__(self):
        self.module_registry = {
            "profile_name": ("memory", "get_profile"),
            "profile_city": ("memory", "get_profile"),
            "preference": ("memory", "get_preference"),
            "task": ("memory", "get_tasks"),
            "conversation": ("memory", "get_conversation"),
            "history": ("memory", "get_history"),
            "general": ("chat", "respond"),
            "delete_files": ("file_manager", "delete"),
            "copy_file": ("file_manager", "copy"),
            "move_file": ("file_manager", "move"),
            "rename_file": ("file_manager", "rename"),
            "open_app": ("app_manager", "open"),
            "close_app": ("app_manager", "close"),
            "shutdown_system": ("system", "shutdown"),
            "restart_system": ("system", "restart"),
        }

    def create_plan(self, context):
        intent = context.get("intent", "general")
        plan = {
            "intent": intent,
            "module": None,
            "action": None,
            "parameters": {},
            "confirmation": False,
            "risk": "low",
            "priority": "normal",
            "steps": [],
            "estimated_time": 0,
            "status": "ready"
        }

        module, action = self.resolve_module(intent)
        plan["module"] = module
        plan["action"] = action
        return self.enrich_plan(plan, context)
    
    def analyze_risk(self, intent):
        high_risk = [
            "delete_files",
            "delete_folder",
            "format_storage",
            "factory_reset",
            "shutdown_system",
            "restart_system",
            "factory_reset_phone",
            "erase_storage"
        ]
        medium_risk = [
            "move_file",
            "rename_file",
            "overwrite_file"
        ]
        if intent in high_risk:
            return "high"

        if intent in medium_risk:
            return "medium"
        return "low"

    def needs_confirmation(self, risk):
        return risk in ["high", "medium"]

    def build_parameters(self, context):
        parameters = {}
        entities = context.get("entities", [])
        if entities:
            parameters["entities"] = entities
        parameters["message"] = context.get("message")
        return parameters

    def enrich_plan(self, plan, context):
        plan["parameters"] = self.build_parameters(context)
        plan["risk"] = self.analyze_risk(plan["intent"])
        plan["confirmation"] = self.needs_confirmation(plan["risk"])
        plan["priority"] = self.calculate_priority(plan["risk"])
        plan["steps"] = self.build_steps(plan)
        plan["estimated_time"] = self.estimate_time(plan["action"])
        return plan

    def build_steps(self, plan):
        action = plan["action"]
        if action == "get_profile":
            return [
                "Read profile data",
                "Return requested value"
            ]
        elif action == "get_preference":
            return [
                "Read preferences",
                "Return preference"
            ]
        elif action == "get_tasks":
            return [
                "Load task list",
                "Return tasks"
            ]
        elif action == "respond":
            return [
                "Generate AI response"
            ]
        elif action == "delete":
            return [
                "Locate target",
                "Verify target exists",
                "Delete target"
            ]
        elif action == "copy":
            return [
                "Locate source",
                "Copy data",
                "Verify copied file"
            ]
        elif action == "move":
            return [
                "Locate source",
                "Move target",
                "Verify destination"
            ]
        elif action == "rename":
            return [
                "Locate file",
                "Rename file",
                "Verify new name"
            ]
        elif action == "open":
            return [
                "Find application",
                "Launch application"
            ]
        elif action == "close":
            return [
                "Find running application",
                "Terminate application"
            ]
        elif action == "shutdown":
            return [
                "Check confirmation",
                "Shutdown system"
            ]
        elif action == "restart":
            return [
                "Check confirmation",
                "Restart system"
            ]
        return [
            "Unknown action"
        ]

    def calculate_priority(self, risk):
        if risk == "high":
            return "high"
        if risk == "medium":
            return "normal"
        return "low"

    def resolve_module(self, intent):
        return self.module_registry.get(
            intent,
            ("chat", "respond")
        )

    def estimate_time(self, action):
        times = {
            "get_profile": 1,
            "get_preference": 1,
            "get_tasks": 1,
            "get_conversation": 1,
            "get_history": 1,
            "respond": 2,
            "open": 3,
            "close": 3,
            "copy": 10,
            "move": 10,
            "rename": 5,
            "delete": 8,
            "shutdown": 5,
            "restart": 10
        }
        return times.get(action, 2)
