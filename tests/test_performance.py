import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import time

from src.planner import Planner
from src.executor import Executor
from src.response_generator import ResponseGenerator

planner = Planner()
executor = Executor()
generator = ResponseGenerator()

question = "My monthly expense is 80000. How much emergency fund should I keep?"

print("=" * 70)

t0 = time.time()

plan = planner.plan(question)

print("Planner:", round(time.time() - t0, 2), "sec")

t1 = time.time()

result = executor.execute(plan)

print("Executor:", round(time.time() - t1, 2), "sec")

t2 = time.time()

answer = generator.generate(
    question=question,
    ground_truth=result["ground_truth"],
)

print("LLM:", round(time.time() - t2, 2), "sec")

print()

print(answer)