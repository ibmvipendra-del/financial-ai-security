import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.llm_planner import LLMPlanner

planner = LLMPlanner()

questions = [

    "My monthly expense is 80000. Calculate emergency fund.",

    "My salary is 120000 and monthly expense is 60000.",

    "Hello"

]

print("=" * 60)

for q in questions:

    print(q)

    print()

    plan = planner.create_plan(q)

    print(plan)

    print("=" * 60)