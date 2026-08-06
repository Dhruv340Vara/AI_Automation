from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from automation.ai.llm.llm_message import (
    LLMMessage,
)

from automation.ai.llm.llm_response import (
    LLMResponse,
)


class LLMAdapter(ABC):
    """
    Base interface for every LLM provider.
    """

    def __init__(
        self,
        model: str,
    ):

        self.model = model

    # ---------------------------- #

    @abstractmethod
    def generate(
        self,
        message: LLMMessage,
    ) -> LLMResponse:
        """
        Generate a response.
        """

    # ---------------------------- #

    @abstractmethod
    def available(
        self,
    ) -> bool:
        """
        Check whether provider is available.
        """

    # ---------------------------- #

    def __repr__(
        self,
    ):

        return (

            f"<{self.__class__.__name__} "

            f"model='{self.model}'>"

        )

