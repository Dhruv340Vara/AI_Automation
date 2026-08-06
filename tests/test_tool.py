from automation.ai.tool import (
    Tool,
)


class DemoTool(
    Tool,
):

    def __init__(self):

        super().__init__(

            name="Demo",

            description="Demo Tool",

        )

    def execute(
        self,
        **kwargs,
    ):

        return {

            "success": True,

            "arguments": kwargs,

        }


tool = DemoTool()

print(tool)

print()

print(tool.is_enabled())

print()

result = tool.execute(

    name="Dhruv",

    age=21,

)

print(result)

print()

tool.disable()

print(tool.is_enabled())

print()

tool.enable()

print(tool.is_enabled())
