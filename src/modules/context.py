import re
from modules.memory import Memory

class ContextEngine:
    def __init__(self):
        self.memory = Memory()

    def build_context(self, user_message):
        user_message = user_message.strip()
        return {
            "message": user_message,
            "intent": self.detect_intent(user_message),
            "entities": self.extract_entities(user_message),
            "memory": self.search_memory(user_message)
        }

    def detect_intent(self, message):
        text = message.lower()
        if any(word in text for word in [
            "name", "naam", "નામ"
        ]):
            return "profile_name"
        if any(word in text for word in [
            "city", "place", "sheher", "શહેર", "ગામ"
        ]):
            return "profile_city"
        if any(word in text for word in [
            "theme", "dark", "light",
            "થીમ", "ડાર્ક", "લાઇટ"
        ]):
            return "preference"
        if any(word in text for word in [
            "task", "todo", "work",
            "ટાસ્ક", "કામ"
        ]):
            return "task"
        return "general"

    def extract_entities(self, message):
        words = re.findall(r"\w+", message)
        return words

    def search_memory(self, message):
        text = message.lower()
        results = {}
        if any(word in text for word in [
            "name", "naam", "નામ"
        ]):
            results["name"] = self.memory.get_profile("name")
        if any(word in text for word in [
            "city", "place", "sheher", "શહેર", "ગામ", "city"
        ]):
            results["city"] = self.memory.get_profile("city")
        if any(word in text for word in [
            "theme", "dark", "light",
            "થીમ", "ડાર્ક", "લાઇટ"
        ]):
            results["theme"] = self.memory.get_preference("theme")
        if any(word in text for word in [
            "task", "todo", "work",
            "ટાસ્ક", "કામ"
        ]):
            results["tasks"] = self.memory.get_tasks()
        results["conversation"] = self.get_recent_conversation(5)
        results["history"] = self.get_recent_history(5)
        return results

    def get_recent_conversation(self, limit=5):
        data = self.memory.get_conversation()
        if len(data) <= limit:
            return data
        return data[-limit:]

    def get_recent_history(self, limit=5):
        data = self.memory.get_history()
        if len(data) <= limit:
            return data
        return data[-limit:]

    def remember_conversation(self, role, message):
        return self.memory.add_conversation(
            role,
            message
        )

    def remember_action(self, action):
        return self.memory.add_history(action)

    def get_context(self, user_message):
        context = self.build_context(user_message)
        self.remember_conversation(
            "user",
            user_message
        )
        self.remember_action(
            f"Context generated for: {user_message}"
        )
        return context
