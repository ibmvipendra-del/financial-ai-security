import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.security_validator import SecurityValidator

validator = SecurityValidator()

print("=" * 60)

plan = {
    "tool": "emergency_fund",
    "arguments": {
        "monthly_expense": 60000
    }
}

print(validator.validate(plan))

print("=" * 60)

try:

    validator.validate(
        {
            "tool": "delete_database",
            "arguments": {}
        }
    )

except Exception as e:

    print(e)

print("=" * 60)