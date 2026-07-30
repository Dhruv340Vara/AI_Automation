from modules.memory import Memory

class Executor:
    def __init__(self):
        self.memory = Memory()
        self.file_manager = None
        self.app_manager = None
        self.system_manager = None
        self.memory_handlers = {
            "get_profile": self.memory_get_profile,
            "get_preference": self.memory_get_preference,
            "get_tasks": self.memory_get_tasks,
            "get_conversation": self.memory_get_conversation,
            "get_history": self.memory_get_history
        }
        self.module_handlers = {
            "memory": self.execute_memory,
            "chat": self.execute_chat,
            "file_manager": self.execute_file_manager,
            "app_manager": self.execute_app_manager,
            "system": self.execute_system
        }

    def execute(self, plan):
        module = plan.get("module")
        handler = self.module_handlers.get(module)
        if handler is None:
            return {
                "success": False,
                "message": f"Unknown module : {module}"
            }
        try:
            return handler(plan)
        except Exception as e:
            return {
                "success": False,
                "message": str(e)
            }

    def is_module_supported(self, module):
        return module in self.module_handlers

    def available_modules(self):
        return list(self.module_handlers.keys())

    def statistics(self):
        return {
            "modules": len(self.module_handlers),
            "memory_actions": len(self.memory_handlers),
            "supported_modules": self.available_modules()
        }

    def execute_memory(self, plan):
        action = plan.get("action")
        handler = self.memory_handlers.get(action)
        if handler is None:
            return {
                "success": False,
                "message": f"Unknown memory action : {action}"
            }
        try:
            return handler(plan)
        except Exception as e:
            return {
                "success": False,
                "message": str(e)
            }

    def memory_get_profile(self, plan):
        parameters = plan.get("parameters", {})
        entities = parameters.get("entities", [])
        message = parameters.get("message", "").lower()
        key = None
        if "name" in entities:
            key = "name"
        elif "city" in entities:
            key = "city"
        elif "name" in message:
            key = "name"
        elif "city" in message:
            key = "city"
        if key is None:
            return {
                "success": False,
                "message": "Profile field not specified."
            }
        return {
            "success": True,
            "data": self.memory.get_profile(key)
        }

    def memory_get_preference(self, plan):
        return {
            "success": True,
            "data": self.memory.get_preference("theme")
        }

    def memory_get_tasks(self, plan):
        return {
            "success": True,
            "data": self.memory.get_tasks()
        }

    def memory_get_conversation(self, plan):
        return {
            "success": True,
            "data": self.memory.get_conversation()
        }

    def memory_get_history(self, plan):
        return {
            "success": True,
            "data": self.memory.get_history()
        }

    def execute_chat(self, plan):
        return {
            "success": True,
            "message": "Chat response placeholder."
        }

    def execute_file_manager(self, plan):
        return {
            "success": False,
            "message": "File Manager not implemented."
        }

    def execute_app_manager(self, plan):
        return {
            "success": False,
            "message": "App Manager not implemented."
        }

    def execute_system(self, plan):
        return {
            "success": False,
            "message": "System Manager not implemented."
        }
