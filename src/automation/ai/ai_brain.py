from __future__ import annotations

from automation.ai.tool_executor import (ToolExecutor,)
from automation.ai.tool_registry import (ToolRegistry,)
from automation.ai.memory_engine import (MemoryEngine,)
from automation.ai.ai_context import (AIContext,)
from automation.ai.ai_message import (AIMessage, MessageRole,)
from automation.ai.ai_session import (AISession,)
from automation.ai.llm.llm_adapter import LLMAdapter
from automation.ai.llm.llm_message import LLMMessage

class AIBrain:

    def __init__(self, llm: LLMAdapter | None = None):
        self.session = AISession()
        self.memory = MemoryEngine()
        self.tool_registry = ToolRegistry()
        self.tool_executor = ToolExecutor(self.tool_registry)
        self.llm = llm

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
        llm_name = (self.llm.__class__.__name__ if self.llm else "None")
        return (f"<AIBrain messages={len(self.context)} active={self.is_active()} llm={llm_name}>")

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

    def ask(self, message: str):
        if self.llm is None:
            raise RuntimeError("LLM is not configured.")
        llm_context = self._build_llm_context()
        user_message = AIMessage(role=MessageRole.USER,content=message,)
        self.receive(user_message)
        llm_message = LLMMessage(user=message,context=llm_context,)
        response = self.llm.generate(llm_message)
        if response.success:
            self.receive(AIMessage(role=MessageRole.ASSISTANT,content=response.content,))
        return response

    def llm_available(self):
        if self.llm is None:
            return False
        return self.llm.available()

    def set_llm(self, llm: LLMAdapter):
        self.llm = llm

    def _build_llm_context(self):
        return {
            "conversation": [
                {"role": message.role.value,"content": message.content,}
                for message in self.context.messages
            ]
        }