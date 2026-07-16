import re


class OutputGuardrail:

    def __init__(self):

        self.rules = [

            (
                "API Key",
                r"api[_\s]?key",
                80,
            ),

            (
                "Password",
                r"password",
                80,
            ),

            (
                "Private Key",
                r"private\s+key",
                90,
            ),

            (
                "System Prompt",
                r"system\s+prompt",
                70,
            ),

            (
                "Ignore Safety",
                r"ignore\s+all\s+rules",
                80,
            ),

            (
                "rm -rf",
                r"rm\s+-rf",
                90,
            ),

            (
                "sudo",
                r"\bsudo\b",
                60,
            ),

            (
                "DELETE DATABASE",
                r"delete\s+database",
                80,
            ),

        ]

    def scan(self, text: str):

        text = text.lower()

        findings = []

        score = 0

        for name, pattern, weight in self.rules:

            if re.search(pattern, text):

                findings.append(name)

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

            "detector": "Output Guardrail",

            "safe": score == 0,

            "score": score,

            "risk": risk,

            "findings": findings,

        }