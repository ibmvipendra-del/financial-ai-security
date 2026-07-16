from src.llm_factory import LLMFactory
from src.ground_truth import GroundTruth


class ResponseGenerator:

    def __init__(self):

        self.llm = LLMFactory.create()

    def generate(

        self,

        question: str,

        ground_truth: GroundTruth,

    ):

        prompt = f"""
You are a professional financial advisor.

The financial calculation has already been performed.

DO NOT perform any calculations.

DO NOT modify any financial values.

Use the verified calculation exactly as provided.

Question:

{question}

Verified Financial Result:

{ground_truth.text}

Explain this result in simple language.

Professional Explanation:
"""

        return self.llm.invoke(prompt)