from dataclasses import dataclass


@dataclass
class BiasResult:

    safe: bool

    score: int

    risk: str

    findings: list


class BiasDetector:
    """
    Enterprise Bias Detector

    Phase 1:
        Compare business decisions instead of raw text.

    Phase 2:
        Integrate Fairlearn / IBM AIF360.
    """

    def scan(
        self,
        decision_a: str,
        decision_b: str,
    ):

        findings = []

        score = 0

        if decision_a != decision_b:

            findings.append(
                f"Decision mismatch: {decision_a} vs {decision_b}"
            )

            score = 100

        if score >= 100:

            risk = "CRITICAL"

        elif score >= 60:

            risk = "HIGH"

        elif score >= 30:

            risk = "MEDIUM"

        else:

            risk = "LOW"

        return BiasResult(

            safe=(score == 0),

            score=score,

            risk=risk,

            findings=findings,

        )