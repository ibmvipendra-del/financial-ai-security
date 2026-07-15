from src.llm_factory import LLMFactory


class ResponseGenerator:

    def __init__(self):

        self.llm = LLMFactory.create()

    def generate(

        self,

        question: str,

        tool_result: str,

    ):

        prompt = f"""
You are a professional financial advisor.

The financial calculation has already been performed.

Do NOT recalculate anything.

Explain the result in simple language.

Question:

{question}

Calculation Result:

{tool_result}

Professional Explanation:
"""

        return self.llm.invoke(prompt)