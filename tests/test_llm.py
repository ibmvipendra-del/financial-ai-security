import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.llm import LLMService


def main():

    llm = LLMService()

    question = """
    I earn ₹1,20,000 per month.

    My expenses are ₹60,000.

    How much emergency fund should I maintain?
    """

    response = llm.invoke(question)

    print("\n")
    print("=" * 80)
    print(response)
    print("=" * 80)


if __name__ == "__main__":
    main()