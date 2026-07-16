import re

from src.ground_truth import GroundTruth


class HallucinationDetector:

    """
    Validates that the LLM preserved
    trusted business values.
    """

    def scan(

        self,

        ground_truth: GroundTruth,

        llm_response: str,

    ):

        findings = []

        score = 0

        if not llm_response.strip():

            findings.append(

                "LLM returned an empty response."

            )

            score += 100

        # --------------------------------------
        # Validate every trusted value
        # --------------------------------------

        for field, expected in ground_truth.values.items():

            expected_text = f"{expected:,.2f}"

            expected_plain = str(int(expected))

            if (

                expected_text not in llm_response

                and expected_plain not in llm_response

            ):

                findings.append(

                    f"{field} expected "

                    f"{expected_text} "

                    "not found."

                )

                score += 100

        # --------------------------------------

        if score >= 100:

            risk = "CRITICAL"

        elif score >= 60:

            risk = "HIGH"

        elif score >= 30:

            risk = "MEDIUM"

        else:

            risk = "LOW"

        return {

            "detector": "Hallucination",

            "safe": score == 0,

            "score": score,

            "risk": risk,

            "findings": findings,

        }