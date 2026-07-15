from src.prompt_injection import PromptInjectionDetector
from src.jailbreak_detector import JailbreakDetector
from src.tool_abuse_detector import ToolAbuseDetector
from src.prompt_leakage_detector import PromptLeakageDetector

from src.security_result import SecurityResult


# ----------------------------------------------------
# Registered Security Detectors
# ----------------------------------------------------

DETECTORS = [

    PromptInjectionDetector(),

    JailbreakDetector(),

    ToolAbuseDetector(),

    PromptLeakageDetector(),

]


class SecurityPipeline:

    detectors = DETECTORS

    def scan(self, prompt: str):

        findings = {}

        overall_score = 0

        safe = True

        attack_types = []

        owasp = set()

        mitre = set()

        # ---------------------------------------------
        # Run every detector
        # ---------------------------------------------

        for detector in self.detectors:

            result = detector.scan(prompt)

            findings[result["detector"]] = result

            overall_score += result["score"]

            if not result["safe"]:

                safe = False

                attack_types.append(result["detector"])

        # ---------------------------------------------
        # Overall Risk
        # ---------------------------------------------

        if overall_score >= 100:

            risk = "CRITICAL"

        elif overall_score >= 60:

            risk = "HIGH"

        elif overall_score >= 30:

            risk = "MEDIUM"

        else:

            risk = "LOW"

        # ---------------------------------------------
        # Recommendation
        # ---------------------------------------------

        recommendation = {

            "LOW": "Allow",

            "MEDIUM": "Review",

            "HIGH": "Block",

            "CRITICAL": "Block Immediately",

        }[risk]

        # ---------------------------------------------
        # Confidence
        # ---------------------------------------------

        confidence = min(1.0, overall_score / 100)

        # ---------------------------------------------
        # OWASP Mapping
        # ---------------------------------------------

        if "Prompt Injection" in attack_types:

            owasp.add("LLM01")
            mitre.add("AML.T0051")

        if "Jailbreak" in attack_types:

            owasp.add("LLM01")
            mitre.add("AML.T0051")

        if "Prompt Leakage" in attack_types:

            owasp.add("LLM02")
            mitre.add("AML.T0010")

        if "Tool Abuse" in attack_types:

            owasp.add("LLM07")
            mitre.add("AML.T0011")

        # ---------------------------------------------
        # Final Security Result
        # ---------------------------------------------

        return SecurityResult(

            safe=safe,

            score=overall_score,

            risk=risk,

            recommendation=recommendation,

            confidence=confidence,

            attack_types=attack_types,

            owasp=sorted(owasp),

            mitre=sorted(mitre),

            detector_results=findings,

        )