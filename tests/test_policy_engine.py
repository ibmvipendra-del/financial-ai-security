import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.policy_engine import PolicyEngine

from src.security_result import SecurityResult


policy = PolicyEngine()


safe_security = SecurityResult(

    safe=True,

    score=0,

    risk="LOW",

    recommendation="Allow",

    confidence=1,

    attack_types=[],

    owasp=[],

    mitre=[],

    detector_results={},

)

unsafe_security = SecurityResult(

    safe=False,

    score=120,

    risk="CRITICAL",

    recommendation="Block",

    confidence=1,

    attack_types=["Prompt Injection"],

    owasp=["LLM01"],

    mitre=["AML.T0051"],

    detector_results={},

)

hallucination = {

    "safe": False,

    "risk": "CRITICAL",

}

guardrail = {

    "safe": False,

    "risk": "HIGH",

}

print("=" * 80)

print(

    policy.evaluate(

        security=safe_security,

    )

)

print("=" * 80)

print(

    policy.evaluate(

        security=unsafe_security,

    )

)

print("=" * 80)

print(

    policy.evaluate(

        security=safe_security,

        hallucination=hallucination,

    )

)

print("=" * 80)

print(

    policy.evaluate(

        security=safe_security,

        output_guardrail=guardrail,

    )

)