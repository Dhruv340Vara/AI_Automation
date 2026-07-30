import json
import os
from datetime import datetime

class Memory:

    def __init__(self):
        self.file = "memory/memory.json"
        self.default_memory = {
            "profile": {},
            "preferences": {},
            "conversation": [],
            "tasks": [],
            "history": []
        }

        if not os.path.exists("memory"):
            os.makedirs("memory")

        if not os.path.exists(self.file):
            self._save(self.default_memory)


    def _load(self):

        try:
            with open(self.file, "r") as f:
                data = json.load(f)

            for key in self.default_memory:
                if key not in data:
                    data[key] = self.default_memory[key]
            return data
        except Exception:
            return self.default_memory.copy()

    def _save(self, data):
        with open(self.file, "w") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)


    def remember(self, key, value):
        reserved = {
            "profile",
            "preferences",
            "conversation",
            "tasks",
            "history"
        }

        if key in reserved:
            return {
                "success": False,
                "message": "Reserved key."
            }

        data = self._load()
        data[key] = value
        self._save(data)
        return {
            "success": True,
            "message": f"{key} saved."
        }

    def recall(self, key):
        data = self._load()
        if key in data:
            return {
                "success": True,
                "value": data[key]
            }
        return {
            "success": False,
            "message": "Memory not found."
        }

    def forget(self, key):
        data = self._load()
        if key in data:
            del data[key]
            self._save(data)
            return {"success": True}
        return {"success": False}

    def set_profile(self, key, value):
        data = self._load()
        data["profile"][key] = value
        self._save(data)
        return {
            "success": True,
            "message": "Profile updated."
        }

    def get_profile(self, key):
        data = self._load()
        value = data["profile"].get(key)
        if value is None:
            return {
                "success": False,
                "message": "Profile value not found."
            }
        return {
            "success": True,
            "value": value
        }

    def set_preference(self, key, value):
        data = self._load()
        data["preferences"][key] = value
        self._save(data)
        return {
            "success": True,
            "message": "Preference saved."
        }

    def get_preference(self, key):
        data = self._load()
        value = data["preferences"].get(key)
        if value is None:
            return {
                "success": False,
                "message": "Preference not found."
            }
        return {
            "success": True,
            "value": value
        }

    def add_conversation(self, role, message):
        data = self._load()
        data["conversation"].append({
            "time": datetime.now().isoformat(),
            "role": role,
            "message": message
        })
        self._save(data)
        return {
            "success": True
        }

    def get_conversation(self):
        return self._load()["conversation"]

    def add_task(self, task):
        data = self._load()
        data["tasks"].append(task)
        self._save(data)
        return {
            "success": True
        }

    def get_tasks(self):
        return self._load()["tasks"]

    def add_history(self, action):
        data = self._load()
        data["history"].append({
            "time": datetime.now().isoformat(),
            "action": action
        })
        self._save(data)
        return {
            "success": True
        }

    def get_history(self):
        return self._load()["history"]

    def all(self):
        return self._load()

    def clear(self):
        self._save(self.default_memory)
        return {
            "success": True,
            "message": "Memory cleared."
        }
