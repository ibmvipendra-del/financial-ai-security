import re


class Planner:
    """
    Planner.

    Current implementation:
        Rule-based planner.

    Future implementation:
        LLM-based planner.

    The rest of the application will always call:

        planner.plan(question)

    regardless of implementation.
    """

    def plan(self, question: str):

        question_lower = question.lower()

        # ------------------------------------------------
        # Emergency Fund
        # ------------------------------------------------

        if "emergency" in question_lower:

            amount = self.extract_number(question)

            return {
                "tool": "emergency_fund",
                "arguments": {
                    "monthly_expense": amount
                }
            }

        # ------------------------------------------------
        # Savings Rate
        # ------------------------------------------------

        if "saving" in question_lower:

            numbers = self.extract_numbers(question)

            if len(numbers) >= 2:

                return {
                    "tool": "savings_rate",
                    "arguments": {
                        "monthly_income": numbers[0],
                        "monthly_expense": numbers[1],
                    },
                }

        # ------------------------------------------------
        # SIP
        # ------------------------------------------------

        if "sip" in question_lower:

            numbers = self.extract_numbers(question)

            if len(numbers) >= 3:

                return {
                    "tool": "sip_calculator",
                    "arguments": {
                        "monthly_investment": numbers[0],
                        "annual_return": numbers[1],
                        "years": int(numbers[2]),
                    },
                }

        # ------------------------------------------------
        # EMI
        # ------------------------------------------------

        if "emi" in question_lower:

            numbers = self.extract_numbers(question)

            if len(numbers) >= 3:

                return {
                    "tool": "emi_calculator",
                    "arguments": {
                        "loan_amount": numbers[0],
                        "annual_rate": numbers[1],
                        "years": int(numbers[2]),
                    },
                }

        # ------------------------------------------------
        # Net Worth
        # ------------------------------------------------

        if "net worth" in question_lower:

            numbers = self.extract_numbers(question)

            if len(numbers) >= 2:

                return {
                    "tool": "net_worth",
                    "arguments": {
                        "total_assets": numbers[0],
                        "total_liabilities": numbers[1],
                    },
                }

        # ------------------------------------------------
        # Default
        # ------------------------------------------------

        return {
            "tool": "chat",
            "arguments": {},
        }

    # ------------------------------------------------

    @staticmethod
    def extract_number(text: str):

        nums = re.findall(r"\d+(?:\.\d+)?", text)

        if nums:

            return float(nums[0])

        return 50000

    # ------------------------------------------------

    @staticmethod
    def extract_numbers(text: str):

        nums = re.findall(r"\d+(?:\.\d+)?", text)

        return [float(x) for x in nums]