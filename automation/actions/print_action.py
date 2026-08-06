from __future__ import annotations


def execute(
    action: dict
):

    print(
        action.get(
            "message",
            ""
        )
    )

    return True
