import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.planner import Planner

planner = Planner()

print("=" * 60)

plan = planner.create_plan(
    "My monthly expense is 80000. How much emergency fund should I keep?"
)

print(plan)

print("=" * 60)

plan = planner.create_plan(
    "Hello"
)

print(plan)

print("=" * 60)