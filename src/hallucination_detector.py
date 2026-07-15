import re


class HallucinationDetector:

    def extract_currency_values(self, text: str):

        """
        Extract only monetary values.

        Ignore things like:
        6 months
        20 years
        12 percent
        """

        matches = re.findall(
            r"₹?\s*([\d,]+(?:\.\d+)?)",
            text,
        )

        values = []

        for value in matches:

            value = value.replace(",", "")

            try:

                values.append(float(value))

            except ValueError:

                pass

        return values

    # -----------------------------------------------------

    def scan(self, tool_result: str, llm_response: str):

        findings = []

        score = 0

        tool_values = self.extract_currency_values(tool_result)

        response_values = self.extract_currency_values(llm_response)

        # ---------------------------------------------

        if len(llm_response.strip()) == 0:

            findings.append("LLM returned an empty response.")

            score += 100

        # ---------------------------------------------

        for value in tool_values:

            found = any(abs(value - x) < 0.01 for x in response_values)

            if not found:

                findings.append(

                    f"Expected value {value:,.2f} missing."

                )

                score += 60

        # ---------------------------------------------

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