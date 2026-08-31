from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from automation.ai.ai_message import (
    AIMessage,
)


@dataclass(slots=True)
class AIContext:
    """
    Stores the current AI conversation context.
    """

    messages: list[AIMessage] = field(
        default_factory=list
    )

    variables: dict[str, Any] = field(
        default_factory=dict
    )

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    # -------------------------------- #

    def add_message(
        self,
        message: AIMessage,
    ):

        self.messages.append(
            message
        )

    # -------------------------------- #

    def last_message(self):

        if not self.messages:
            return None

        return self.messages[-1]

    # -------------------------------- #

    def clear_messages(self):

        self.messages.clear()

    # -------------------------------- #

    def set_variable(
        self,
        key: str,
        value: Any,
    ):

        self.variables[key] = value

    # -------------------------------- #

    def get_variable(
        self,
        key: str,
        default=None,
    ):

        return self.variables.get(
            key,
            default,
        )

    # -------------------------------- #

    def remove_variable(
        self,
        key: str,
    ):

        return self.variables.pop(
            key,
            None,
        )

    # -------------------------------- #

    def clear_variables(self):

        self.variables.clear()

    # -------------------------------- #

    def count_messages(self):

        return len(
            self.messages
        )

    # -------------------------------- #

    def to_dict(self):

        return {

            "messages": [

                message.to_dict()

                for message in self.messages

            ],

            "variables": self.variables,

            "metadata": self.metadata,

        }

    # -------------------------------- #

    @classmethod
    def from_dict(
        cls,
        data: dict,
    ):

        context = cls()

        context.messages = [

            AIMessage.from_dict(
                message
            )

            for message in data.get(
                "messages",
                [],
            )

        ]

        context.variables = data.get(
            "variables",
            {},
        )

        context.metadata = data.get(
            "metadata",
            {},
        )

        return context

    # -------------------------------- #

    def __len__(self):

        return len(
            self.messages
        )

    # -------------------------------- #

    def __repr__(self):

        return (
            "<AIContext "
            f"messages={len(self.messages)} "
            f"variables={len(self.variables)}>"
        )
