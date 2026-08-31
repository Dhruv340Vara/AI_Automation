from __future__ import annotations

from automation.ai.tool_executor import (ToolExecutor,)
from automation.ai.tool_registry import (ToolRegistry,)
from automation.ai.memory_engine import (MemoryEngine,)
from automation.ai.ai_context import (AIContext,)
from automation.ai.ai_message import (AIMessage,)
from automation.ai.ai_session import (AISession,)

class AIBrain:

    def __init__(self):
        self.session = AISession()
        self.memory = MemoryEngine()
        self.tool_registry = ToolRegistry()
        self.tool_executor = ToolExecutor(self.tool_registry)

    @property
    def context(self) -> AIContext:
        return self.session.context

    def receive(self,message: AIMessage,):
        self.context.add_message(message)
        self.session.touch()
        return message

    def history(self):
        return list(self.context.messages)

    def last_message(self):
        return self.context.last_message()

    def clear(self):
        self.session.reset()

    def close(self):
        self.session.close()

    def open(self):
        self.session.open()

    def is_active(self):
        return self.session.is_active()

    def __repr__(self):
        return (f"<AIBrain messages={len(self.context)} active={self.is_active()}>")

    def remember(self,key: str,value,):
        self.memory.set(key,value,)

    def recall(self,key: str,default=None,):
        return self.memory.get(key,default,)

    def forget(self,key: str,):
        return self.memory.remove(key,)

    def search_memory(self,keyword: str,):
        return self.memory.search(keyword,)

    def clear_memory(self,):
        self.memory.clear()

    def register_tool(self,tool,):
        return self.tool_registry.register(tool)

    def unregister_tool(self,name: str,):
        return self.tool_registry.unregister(name)

    def execute_tool(self,tool_name: str,**kwargs,):
        return self.tool_executor.execute(tool_name,**kwargs,)

    def available_tools(self,):
        return self.tool_registry.names()