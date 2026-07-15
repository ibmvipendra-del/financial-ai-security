from src.graph import graph
from src.security_pipeline import SecurityPipeline


class FinancialAIAgent:

    def __init__(self):

        self.security = SecurityPipeline()

    def invoke(self, question: str):

        security_result = self.security.scan(question)

        if not security_result["safe"]:

            return {

                "question": question,

                "answer": "Request blocked by AI Security Pipeline.",

                "security": security_result,

            }

        response = graph.invoke(
            {
                "question": question
            }
        )

        response["security"] = security_result

        return response