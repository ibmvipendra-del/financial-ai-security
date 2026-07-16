import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.ground_truth_builder import GroundTruthBuilder

builder = GroundTruthBuilder()

cases = [

    (

        "emergency_fund",

        "Recommended Emergency Fund (6 months): ₹480,000.00",

    ),

    (

        "net_worth",

        "Net Worth: ₹5,500,000.00",

    ),

]

print("=" * 80)

for tool, text in cases:

    print(text)

    print()

    print(

        builder.build(

            tool,

            text,

        )

    )

    print("-" * 80)