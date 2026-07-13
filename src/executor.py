from src.tools import TOOL_REGISTRY


class ToolExecutor:
    """
    Executes the tool selected by the planner.
    """

    def execute(self, plan: dict):

        tool_name = plan.get("tool")
        arguments = plan.get("arguments", {})

        # Chat requests don't need a tool
        if tool_name == "chat":
            return None

        # Allow only registered tools
        if tool_name not in TOOL_REGISTRY:
            raise ValueError(
                f"Unauthorized tool requested: {tool_name}"
            )

        tool = TOOL_REGISTRY[tool_name]

        return tool.invoke(arguments)