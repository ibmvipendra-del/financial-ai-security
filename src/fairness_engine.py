from src.bias_detector import BiasDetector
from src.decision_extractor import DecisionExtractor
from src.fairness_case import FairnessCase


class FairnessEngine:

    def __init__(self, agent):

        self.agent = agent

        self.detector = BiasDetector()

        self.extractor = DecisionExtractor()

    def evaluate(self, case: FairnessCase):

        print("\nRunning Prompt A...")

        result_a = self.agent.invoke(case.prompt_a)

        print("\nRunning Prompt B...")

        result_b = self.agent.invoke(case.prompt_b)

        response_a = result_a.get("answer", "")

        response_b = result_b.get("answer", "")

        decision_a = self.extractor.extract(response_a)

        decision_b = self.extractor.extract(response_b)

        bias_result = self.detector.scan(

            decision_a,

            decision_b,

        )

        return {

            "attribute": case.attribute,

            "value_a": case.value_a,

            "value_b": case.value_b,

            "prompt_a": case.prompt_a,

            "prompt_b": case.prompt_b,

            "response_a": response_a,

            "response_b": response_b,

            "decision_a": decision_a,

            "decision_b": decision_b,

            "bias": bias_result,

        }