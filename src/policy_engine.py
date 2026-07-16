from dataclasses import dataclass


@dataclass
class PolicyDecision:

    allow: bool

    reason: str

    severity: str


class PolicyEngine:

    def evaluate(

        self,

        security=None,

        hallucination=None,

        output_guardrail=None,

    ):

        # -----------------------------
        # Input Security
        # -----------------------------

        if security is not None:

            if not security.safe:

                return PolicyDecision(

                    allow=False,

                    severity=security.risk,

                    reason="Blocked by Security Pipeline",

                )

        # -----------------------------
        # Hallucination
        # -----------------------------

        if hallucination is not None:

            if not hallucination["safe"]:

                return PolicyDecision(

                    allow=False,

                    severity=hallucination["risk"],

                    reason="Hallucination Detected",

                )

        # -----------------------------
        # Output Guardrail
        # -----------------------------

        if output_guardrail is not None:

            if not output_guardrail["safe"]:

                return PolicyDecision(

                    allow=False,

                    severity=output_guardrail["risk"],

                    reason="Unsafe Output",

                )

        return PolicyDecision(

            allow=True,

            severity="LOW",

            reason="Policy Passed",

        )