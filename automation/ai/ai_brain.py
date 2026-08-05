from __future__ import annotations

from automation.ai.ai_context import (
    AIContext,
)

from automation.ai.ai_message import (
    AIMessage,
)

from automation.ai.ai_session import (
    AISession,
)


class AIBrain:
    """
    Core AI Brain.

    Responsible for managing
    session and conversation state.

    Future phases will extend this
    class with:

    - Intent Recognition
    - Planning
    - Memory
    - Tool Selection
    - Automation Generation
    """

    def __init__(self):

        self.session = AISession()

    # -------------------------------- #

    @property
    def context(self) -> AIContext:

        return self.session.context

    # -------------------------------- #

    def receive(
        self,
        message: AIMessage,
    ):

        self.context.add_message(
            message
        )

        self.session.touch()

        return message

    # -------------------------------- #

    def history(self):

        return list(
            self.context.messages
        )

    # -------------------------------- #

    def last_message(self):

        return self.context.last_message()

    # -------------------------------- #

    def clear(self):

        self.session.reset()

    # -------------------------------- #

    def close(self):

        self.session.close()

    # -------------------------------- #

    def open(self):

        self.session.open()

    # -------------------------------- #

    def is_active(self):

        return self.session.is_active()

    # -------------------------------- #

    def __repr__(self):

        return (
            "<AIBrain "
            f"messages={len(self.context)} "
            f"active={self.is_active()}>"
        )
