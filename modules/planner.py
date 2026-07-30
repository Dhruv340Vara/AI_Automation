class Planner:
    def __init__(self):
        pass

    def create_plan(self, context):
        intent = context.get("intent", "general")
        plan = {
            "intent": intent,
            "module": None,
            "action": None,
            "parameters": {},
            "confirmation": False,
            "risk": "low",
            "status": "ready"
        }

        if intent == "profile_name":
            plan["module"] = "memory"
            plan["action"] = "get_profile"
        elif intent == "profile_city":
            plan["module"] = "memory"
            plan["action"] = "get_profile"

        elif intent == "preference":
            plan["module"] = "memory"
            plan["action"] = "get_preference"

        elif intent == "task":
            plan["module"] = "memory"
            plan["action"] = "get_tasks"

        else:
            plan["module"] = "chat"
            plan["action"] = "respond"
        return self.enrich_plan(plan, context)
    
    def analyze_risk(self, intent):
        high_risk = [
            "delete_files",
            "delete_folder",
            "format_storage",
            "factory_reset"
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
        plan["risk"] = self.analyze_risk(
            plan["intent"]
        )
        plan["confirmation"] = self.needs_confirmation(
            plan["risk"]
        )
        return plan
