import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.tools import (
    emergency_fund,
    savings_rate,
    sip_calculator,
    emi_calculator,
    net_worth,
)


print("=" * 60)

print(
    emergency_fund.invoke(
        {
            "monthly_expense": 50000,
            "months": 6,
        }
    )
)

print(
    savings_rate.invoke(
        {
            "monthly_income": 120000,
            "monthly_expense": 60000,
        }
    )
)

print(
    sip_calculator.invoke(
        {
            "monthly_investment": 10000,
            "annual_return": 12,
            "years": 20,
        }
    )
)

print(
    emi_calculator.invoke(
        {
            "loan_amount": 5000000,
            "annual_rate": 8.5,
            "years": 20,
        }
    )
)

print(
    net_worth.invoke(
        {
            "total_assets": 9000000,
            "total_liabilities": 3000000,
        }
    )
)

print("=" * 60)