import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.hallucination_detector import HallucinationDetector

detector = HallucinationDetector()

cases = [

    (
        "Recommended Emergency Fund (6 months): ₹480,000.00",
        "You should maintain an emergency fund of ₹480,000."
    ),

    (
        "Recommended Emergency Fund (6 months): ₹480,000.00",
        "You should maintain an emergency fund of ₹600,000."
    ),

    (
        "Recommended Emergency Fund (6 months): ₹480,000.00",
        ""
    ),

]

print("=" * 80)

for tool_result, llm_response in cases:

    print("Tool Result:")
    print(tool_result)

    print()

    print("LLM Response:")
    print(llm_response)

    print()

    print(detector.scan(tool_result, llm_response))

    print("-" * 80)