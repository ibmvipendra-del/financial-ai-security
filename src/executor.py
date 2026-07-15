from src.tools import TOOL_REGISTRY


class Executor:

    def execute(self, plan: dict):

        tool_name = plan["tool"]

        if tool_name == "chat":

            return {
                "tool_result": None,
                "answer": None,
            }

        tool = TOOL_REGISTRY.get(tool_name)

        if tool is None:

            raise ValueError(
                f"Unknown tool: {tool_name}"
            )

        result = tool.invoke(
            plan["arguments"]
        )

        return {

            "tool_result": result,

            "answer": result,

        }