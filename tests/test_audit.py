import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.audit import AuditLogger

logger = AuditLogger()

logger.log(

    question="How much emergency fund should I keep?",

    plan={
        "tool": "emergency_fund",
        "arguments": {
            "monthly_expense": 50000
        }
    },

    answer="Recommended Emergency Fund (6 months): ₹300,000.00",

    risk="LOW"

)

print("=" * 60)
print("Audit log created successfully.")
print("=" * 60)