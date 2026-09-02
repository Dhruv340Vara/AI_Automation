from __future__ import annotations

from automation.ai.tool_executor import (ToolExecutor,)
from automation.ai.tool_registry import (ToolRegistry,)
from automation.ai.memory_engine import (MemoryEngine,)
from automation.ai.ai_context import (AIContext,)
from automation.ai.ai_message import (AIMessage, MessageRole,)
from automation.ai.ai_session import (AISession,)
from automation.ai.llm.llm_adapter import LLMAdapter
from automation.ai.llm.llm_message import LLMMessage
from automation.ai.tool_call_parser import ToolCallParser

class AIBrain:

    def __init__(self, llm: LLMAdapter | None = None, max_history: int = 20,):
        self.session = AISession()
        self.memory = MemoryEngine()
        self.tool_registry = ToolRegistry()
        self.tool_executor = ToolExecutor(self.tool_registry)
        self.llm = llm
        self.max_history = max_history

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

    def execute_tool_call(self, tool_call):
        """
        Execute a parsed ToolCall through the ToolExecutor.
        """

        return self.tool_executor.execute(
            tool_call.tool,
            **tool_call.arguments,
        )

    def available_tools(self,):
        return self.tool_registry.names()

    def ask(self, message: str):
        if self.llm is None:
            raise RuntimeError("LLM is not configured.")

        # 1. Retrieve relevant memories BEFORE saving current message
        llm_context = self._build_llm_context(query=message)

        # 2. Add user message to short-term conversation
        user_message = AIMessage(
            role=MessageRole.USER,
            content=message,
        )
        self.receive(user_message)

        # 3. Automatically save user message to long-term memory
        user_importance = self.memory.calculate_importance(
            content=message,
            role="user",
        )

        self.memory.remember_conversation(
            role="user",
            content=message,
            importance=user_importance,
        )

        # 4. Send request to LLM
        tool_prompt = self._tool_selection_system_prompt()

        llm_message = LLMMessage(
            system=tool_prompt,
            user=message,
            context=llm_context,
        )

        response = self.llm.generate(llm_message)

        # 5. Parse structured LLM response
        if response.success:
            try:
                decision = ToolCallParser.parse(response.content)

                response.set_metadata(
                    "response_type",
                    decision["type"],
                )

                if decision["type"] == "tool_call":
                    tool_call = decision["tool_call"]

                    response.set_metadata(
                        "tool_call",
                        tool_call.to_dict(),
                    )

                    tool_result = self.execute_tool_call(
                        tool_call
                    )

                    tool_result_data = {
                        "success": tool_result.success,
                        "data": tool_result.data,
                        "message": tool_result.message,
                        "metadata": tool_result.metadata,
                    }

                    response.set_metadata(
                        "tool_result",
                        tool_result_data,
                    )

                    # ---------------------------------
                    # Send Tool Result back to LLM
                    # ---------------------------------

                    result_message = self._build_tool_result_message(
                        tool_call=tool_call,
                        tool_result=tool_result,
                    )

                    final_response = self.llm.generate(
                        result_message
                    )

                    if final_response.success:

                        try:
                            final_decision = ToolCallParser.parse(
                                final_response.content
                            )

                            if final_decision["type"] != "final_answer":
                                raise ValueError(
                                    "Expected final_answer from LLM"
                                )

                            response.set_metadata(
                                "final_response",
                                final_response.content,
                            )

                            response.set_metadata(
                                "final_answer",
                                final_decision["content"],
                            )

                            response.content = final_decision["content"]

                        except (TypeError, ValueError) as exc:

                            response.set_metadata(
                                "final_response_parse_error",
                                str(exc),
                            )

                            response.content = (
                                final_response.content
                            )

                    else:
                        response.set_metadata(
                            "final_response_error",
                            final_response.content,
                        )

                elif decision["type"] == "final_answer":
                    response.set_metadata(
                        "final_answer",
                        decision["content"],
                    )

            except (TypeError, ValueError) as exc:
                response.set_metadata(
                    "response_type",
                    "raw",
                )
                response.set_metadata(
                    "parse_error",
                    str(exc),
                )

        # 6. Save assistant response
        if response.success:
            assistant_message = AIMessage(
                role=MessageRole.ASSISTANT,
                content=response.content,
            )

            # Short-term history
            self.receive(assistant_message)

            # Long-term memory
            assistant_importance = self.memory.calculate_importance(
                content=response.content,
                role="assistant",
            )

            self.memory.remember_conversation(
                role="assistant",
                content=response.content,
                importance=assistant_importance,
            )

        return response

    def llm_available(self):
        if self.llm is None:
            return False
        return self.llm.available()

    def set_llm(self, llm: LLMAdapter):
        self.llm = llm

    def _build_llm_context(self,query: str = "",memory_limit: int = 5,):
        messages = self.context.messages

        if self.max_history <= 0:
            messages = []
        else:
            messages = messages[-self.max_history:]

        relevant_memories = self._retrieve_relevant_memories(
            query=query,
            limit=memory_limit,
        )

        return {
            "conversation": [
                {
                    "role": message.role.value,
                    "content": message.content,
                }
                for message in messages
            ],
            "memories": relevant_memories,
            "tools": self.available_tool_schemas(),
        }

    def _retrieve_relevant_memories(self,query: str,limit: int = 5,) -> list[dict]:

        if not query.strip():
            return []

        try:
            memories = self.memory.search_conversation(
                query=query,
                limit=limit,
            )

            return memories

        except Exception:
            return []

    def available_tool_schemas(self):
        return self.tool_registry.schemas()

    def _tool_selection_system_prompt(self) -> str:
        return """
            You are an AI assistant with access to external tools.

            Your job is to decide whether the user's request requires using a tool.

            You MUST return exactly one valid JSON object.

            If a tool is required, return:
            {
            "type": "tool_call",
            "tool": "<tool name>",
            "arguments": {}
            }

            If no tool is required, return:
            {
            "type": "final_answer",
            "content": "<your answer>"
            }

            Rules:
            1. Use only tools provided in the available tools list.
            2. Never invent a tool name.
            3. Tool arguments must always be a JSON object.
            4. Do not use Markdown code fences.
            5. Do not add explanations outside the JSON object.
            6. If the request can be answered normally without a tool, use "final_answer".
            7. If a tool is clearly required, use "tool_call".
            8. Tool names are case-sensitive.
            9. You MUST use the exact tool name from the Available Tools list.
            10. Never change the capitalization of a tool name.
            """

    def _build_tool_result_message(self,tool_call,tool_result,) -> LLMMessage:

        return LLMMessage(
            system="""
                You are an AI assistant.

                A tool was executed for the user's request.

                Use the tool result to answer the user.

                Return exactly one valid JSON object:

                {
                    "type": "final_answer",
                    "content": "<natural language answer>"
                }

                Rules:
                1. Use the tool result accurately.
                2. Do not invent information.
                3. Do not call another tool in this step.
                4. Do not use Markdown code fences.
                5. Do not add anything outside the JSON object.
            """,
            user=self.context.messages[-1].content,
            context={
                "tool_call": tool_call.to_dict(),
                "tool_result": {
                    "success": tool_result.success,
                    "data": tool_result.data,
                    "message": tool_result.message,
                    "metadata": tool_result.metadata,
                },
            },
        )