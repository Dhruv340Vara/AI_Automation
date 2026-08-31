from automation.ai.tool_result import (
    ToolResult,
)

result = ToolResult(

    success=True,

    data={

        "folder":

        "Downloads"

    },

    message="Folder created",

)

result.set_metadata(

    "tool",

    "File",

)

print(result)

print()

print(

    result.is_success()

)

print()

print(

    result.to_dict()

)

print()

copy = ToolResult.from_dict(

    result.to_dict()

)

print(copy)

print()

print(

    copy.get_metadata(

        "tool"

    )

)
