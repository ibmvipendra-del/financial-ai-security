import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.planner import Planner

planner = Planner()

questions = [

    "My monthly expense is 80000. Calculate emergency fund.",

    "My salary is 120000 and expense is 60000. Calculate savings rate.",

    "SIP 10000 at 12 percent for 20 years.",

    "EMI for 5000000 loan at 8 percent for 20 years.",

    "My assets are 8000000 and liabilities are 2500000. Calculate net worth.",

    "Hello",

]

print("=" * 70)

for q in questions:

    print(q)

    print(planner.plan(q))

    print("-" * 70)