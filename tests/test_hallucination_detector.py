import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.ground_truth import GroundTruth
from src.hallucination_detector import HallucinationDetector


detector = HallucinationDetector()


ground_truth = GroundTruth(

    tool="emergency_fund",

    text="Recommended Emergency Fund (6 months): ₹480,000.00",

    values={

        "emergency_fund":480000

    }

)


cases = [

    "You should maintain an emergency fund of ₹480,000.00.",

    "You should maintain an emergency fund of ₹600,000.",

    "",

]


print("=" * 80)

for response in cases:

    print("Ground Truth:")

    print(ground_truth)

    print()

    print("LLM Response:")

    print(response)

    print()

    print(

        detector.scan(

            ground_truth,

            response,

        )

    )

    print("-" * 80)