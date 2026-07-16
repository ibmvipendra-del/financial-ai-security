import re

from src.ground_truth import GroundTruth


class GroundTruthBuilder:

    def build(self, tool_name: str, tool_output: str):

        values = {}

        # -----------------------------------------
        # Emergency Fund
        # -----------------------------------------

        if tool_name == "emergency_fund":

            match = re.search(
                r"₹([\d,]+(?:\.\d+)?)",
                tool_output,
            )

            if match:

                amount = float(
                    match.group(1).replace(",", "")
                )

                values["emergency_fund"] = amount

        # -----------------------------------------
        # Savings Rate
        # -----------------------------------------

        elif tool_name == "savings_rate":

            match = re.search(
                r"([\d.]+)%",
                tool_output,
            )

            if match:

                values["savings_rate"] = float(match.group(1))

        # -----------------------------------------
        # SIP
        # -----------------------------------------

        elif tool_name == "sip_calculator":

            match = re.search(
                r"₹([\d,]+(?:\.\d+)?)",
                tool_output,
            )

            if match:

                values["future_value"] = float(
                    match.group(1).replace(",", "")
                )

        # -----------------------------------------
        # EMI
        # -----------------------------------------

        elif tool_name == "emi_calculator":

            match = re.search(
                r"₹([\d,]+(?:\.\d+)?)",
                tool_output,
            )

            if match:

                values["monthly_emi"] = float(
                    match.group(1).replace(",", "")
                )

        # -----------------------------------------
        # Net Worth
        # -----------------------------------------

        elif tool_name == "net_worth":

            match = re.search(
                r"₹([\d,]+(?:\.\d+)?)",
                tool_output,
            )

            if match:

                values["net_worth"] = float(
                    match.group(1).replace(",", "")
                )

        return GroundTruth(

            tool=tool_name,

            text=tool_output,

            values=values,

        )