from __future__ import annotations

from enum import Enum


class IntentType(Enum):
    """
    Supported AI intent types.
    """

    # -------------------------------- #
    # Conversation
    # -------------------------------- #

    CHAT = "chat"

    QUESTION = "question"

    UNKNOWN = "unknown"

    # -------------------------------- #
    # Automation
    # -------------------------------- #

    CREATE_AUTOMATION = (
        "create_automation"
    )

    UPDATE_AUTOMATION = (
        "update_automation"
    )

    DELETE_AUTOMATION = (
        "delete_automation"
    )

    RUN_AUTOMATION = (
        "run_automation"
    )

    STOP_AUTOMATION = (
        "stop_automation"
    )

    ENABLE_AUTOMATION = (
        "enable_automation"
    )

    DISABLE_AUTOMATION = (
        "disable_automation"
    )

    LIST_AUTOMATIONS = (
        "list_automations"
    )

    # -------------------------------- #
    # Runtime
    # -------------------------------- #

    START_RUNTIME = (
        "start_runtime"
    )

    STOP_RUNTIME = (
        "stop_runtime"
    )

    RUNTIME_STATUS = (
        "runtime_status"
    )

    # -------------------------------- #
    # File Operations
    # -------------------------------- #

    FILE_OPERATION = (
        "file_operation"
    )

    # -------------------------------- #
    # Web / API
    # -------------------------------- #

    WEBHOOK = "webhook"

    API = "api"

    # -------------------------------- #
    # Search
    # -------------------------------- #

    SEARCH = "search"

    # -------------------------------- #

    @classmethod
    def values(cls):

        return [
            member.value
            for member in cls
        ]

    # -------------------------------- #

    @classmethod
    def names(cls):

        return [
            member.name
            for member in cls
        ]

    # -------------------------------- #

    @classmethod
    def has_value(
        cls,
        value: str,
    ):

        return (
            value in cls.values()
        )
