from langchain_core.tools import tool


@tool
def emergency_fund(monthly_expense: float, months: int = 6) -> str:
    """Calculate the recommended emergency fund based on monthly expenses."""

    amount = monthly_expense * months
    return f"Recommended Emergency Fund ({months} months): ₹{amount:,.2f}"


@tool
def savings_rate(monthly_income: float, monthly_expense: float) -> str:
    """Calculate the monthly savings rate."""

    savings = monthly_income - monthly_expense
    rate = (savings / monthly_income) * 100

    return f"Savings Rate: {rate:.2f}% (₹{savings:,.2f} saved monthly)"


@tool
def sip_calculator(
    monthly_investment: float,
    annual_return: float,
    years: int,
) -> str:
    """Calculate the future value of a SIP investment."""

    r = annual_return / 100 / 12
    n = years * 12

    future_value = (
        monthly_investment
        * (((1 + r) ** n - 1) / r)
        * (1 + r)
    )

    return f"SIP Value: ₹{future_value:,.2f}"


@tool
def emi_calculator(
    loan_amount: float,
    annual_rate: float,
    years: int,
) -> str:
    """Calculate the EMI for a loan."""

    r = annual_rate / 12 / 100
    n = years * 12

    emi = (
        loan_amount
        * r
        * (1 + r) ** n
        / ((1 + r) ** n - 1)
    )

    return f"Monthly EMI: ₹{emi:,.2f}"


@tool
def net_worth(
    total_assets: float,
    total_liabilities: float,
) -> str:
    """Calculate a user's net worth."""

    worth = total_assets - total_liabilities

    return f"Net Worth: ₹{worth:,.2f}"