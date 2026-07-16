from src.tools import TOOL_REGISTRY
from src.ground_truth_builder import GroundTruthBuilder


class Executor:

    def __init__(self):

        self.builder = GroundTruthBuilder()

    def execute(self, plan: dict):

        tool_name = plan["tool"]

        # -----------------------------
        # Chat
        # -----------------------------

        if tool_name == "chat":

            return {

                "tool_result": None,

                "ground_truth": None,

                "answer": None,

            }

        # -----------------------------
        # Get Tool
        # -----------------------------

        tool = TOOL_REGISTRY.get(tool_name)

        if tool is None:

            raise ValueError(
                f"Unknown tool: {tool_name}"
            )

        # -----------------------------
        # Execute Tool
        # -----------------------------

        tool_output = tool.invoke(
            plan["arguments"]
        )

        # -----------------------------
        # Build Ground Truth
        # -----------------------------

        ground_truth = self.builder.build(

            tool_name,

            tool_output,

        )

        # -----------------------------
        # Return
        # -----------------------------

        return {

            "tool_result": tool_output,

            "ground_truth": ground_truth,

            "answer": tool_output,

        }