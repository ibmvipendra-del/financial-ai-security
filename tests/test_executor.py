import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.executor import Executor

executor = Executor()

print("=" * 60)

response = executor.execute(

    {

        "tool": "emergency_fund",

        "arguments": {

            "monthly_expense": 90000

        }

    }

)

print(response)

print("=" * 60)

response = executor.execute(

    {

        "tool": "chat",

        "arguments": {}

    }

)

print(response)