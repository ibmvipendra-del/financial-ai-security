import json

from src.llm_factory import LLMFactory


class LLMPlanner:

    def __init__(self):

        self.llm = LLMFactory.create()

    def create_plan(self, question: str):

        prompt = f"""
You are an AI Planner.

Available tools:

1. emergency_fund(monthly_expense)

2. savings_rate(monthly_income, monthly_expense)

3. sip_calculator(monthly_investment, annual_return, years)

4. emi_calculator(loan_amount, annual_rate, years)

5. net_worth(total_assets, total_liabilities)

If a tool should be used,
return ONLY valid JSON.

Example:

{{
    "tool":"emergency_fund",
    "arguments":{{
        "monthly_expense":50000
    }}
}}

If no tool is needed return

{{
    "tool":"chat",
    "arguments":{{}}
}}

User Question:

{question}
"""

        response = self.llm.invoke(prompt)

        if hasattr(response, "content"):
            response = response.content

        try:
            return json.loads(response)

        except Exception:

            return {
                "tool": "chat",
                "arguments": {}
            }