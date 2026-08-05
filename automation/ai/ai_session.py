from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
import uuid

from automation.ai.ai_context import (
    AIContext,
)


@dataclass(slots=True)
class AISession:
    """
    Represents one AI session.
    """

    session_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    context: AIContext = field(
        default_factory=AIContext
    )

    created_at: datetime = field(
        default_factory=datetime.utcnow
    )

    updated_at: datetime = field(
        default_factory=datetime.utcnow
    )

    active: bool = True

    # -------------------------------- #

    def touch(self):

        self.updated_at = datetime.utcnow()

    # -------------------------------- #

    def reset(self):

        self.context = AIContext()

        self.touch()

    # -------------------------------- #

    def close(self):

        self.active = False

        self.touch()

    # -------------------------------- #

    def open(self):

        self.active = True

        self.touch()

    # -------------------------------- #

    def is_active(self):

        return self.active

    # -------------------------------- #

    def to_dict(self):

        return {

            "session_id": self.session_id,

            "context": self.context.to_dict(),

            "created_at": self.created_at.isoformat(),

            "updated_at": self.updated_at.isoformat(),

            "active": self.active,

        }

    # -------------------------------- #

    @classmethod
    def from_dict(
        cls,
        data: dict,
    ):

        return cls(

            session_id=data["session_id"],

            context=AIContext.from_dict(
                data["context"]
            ),

            created_at=datetime.fromisoformat(
                data["created_at"]
            ),

            updated_at=datetime.fromisoformat(
                data["updated_at"]
            ),

            active=data.get(
                "active",
                True,
            ),

        )

    # -------------------------------- #

    def __repr__(self):

        state = (
            "active"
            if self.active
            else "closed"
        )

        return (

            "<AISession "

            f"{state} "

            f"messages={len(self.context)}>"

        )
