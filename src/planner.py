import re


class Planner:
    """
    Planner is responsible for understanding the user's request
    and deciding which tool should be executed.

    Currently it uses simple rule-based logic.
    Later it will be replaced by the LLM.
    """

    def create_plan(self, question: str) -> dict:

        question_lower = question.lower()

        # Emergency Fund
        if "emergency" in question_lower:

            numbers = re.findall(r"\d+", question)

            monthly_expense = 50000

            if numbers:
                monthly_expense = float(numbers[0])

            return {
                "tool": "emergency_fund",
                "arguments": {
                    "monthly_expense": monthly_expense
                }
            }

        # Savings Rate
        if "saving" in question_lower:

            return {
                "tool": "savings_rate",
                "arguments": {}
            }

        # SIP
        if "sip" in question_lower:

            return {
                "tool": "sip_calculator",
                "arguments": {}
            }

        # EMI
        if "emi" in question_lower:

            return {
                "tool": "emi_calculator",
                "arguments": {}
            }

        # Net Worth
        if "net worth" in question_lower:

            return {
                "tool": "net_worth",
                "arguments": {}
            }

        # General Chat

        return {
            "tool": "chat",
            "arguments": {}
        }