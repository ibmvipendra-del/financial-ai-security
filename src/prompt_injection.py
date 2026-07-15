import re

from src.risk_engine import RiskEngine


class PromptInjectionDetector:
    """
    Detect Prompt Injection attacks before
    they reach the LLM.
    """

    def __init__(self):

        self.risk_engine = RiskEngine()

        self.patterns = [

            # Prompt Manipulation
            r"ignore\s+previous",
            r"ignore\s+all",
            r"ignore\s+instructions",
            r"forget\s+previous",
            r"override",

            # Prompt Leakage
            r"system\s+prompt",
            r"developer\s+message",
            r"reveal\s+prompt",
            r"show\s+prompt",
            r"print\s+prompt",

            # Secrets
            r"api\s*key",
            r"password",
            r"secret",

            # Dangerous Commands
            r"delete\s+database",
            r"shutdown",
            r"sudo",
            r"rm\s+-rf",

            # Security Bypass
            r"disable\s+security",
            r"bypass",
        ]

    def scan(self, prompt: str):

        text = prompt.lower()

        findings = []

        for pattern in self.patterns:

            if re.search(pattern, text):

                findings.append(pattern)

        risk = self.risk_engine.calculate(findings)

        return {

            "safe": len(findings) == 0,

            "matches": findings,

            "score": risk["score"],

            "risk": risk["level"],

        }