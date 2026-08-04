from __future__ import annotations


def execute(
    action: dict
):

    function = action["function"]

    args = action.get(
        "args",
        []
    )

    kwargs = action.get(
        "kwargs",
        {}
    )

    function(
        *args,
        **kwargs
    )

    return True
