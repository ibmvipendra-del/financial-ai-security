import re


class BaseDetector:

    RULES = []

    DETECTOR_NAME = "Base"

    def scan(self, prompt: str):

        prompt = prompt.lower()

        matches = []

        score = 0

        for pattern, weight in self.RULES:

            if re.search(pattern, prompt):

                matches.append(pattern)

                score += weight

        if score >= 100:
            risk = "CRITICAL"

        elif score >= 60:
            risk = "HIGH"

        elif score >= 30:
            risk = "MEDIUM"

        else:
            risk = "LOW"

        return {

            "detector": self.DETECTOR_NAME,

            "safe": score == 0,

            "score": score,

            "risk": risk,

            "matches": matches,

        }