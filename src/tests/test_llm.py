import sys
from pathlib import Path

# Add project root to Python path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.llm import LLMService


def test_llm():
    llm = LLMService()

    response = llm.invoke(
        "Explain emergency fund in one sentence."
    )

    print("\n===== RESPONSE =====\n")
    print(response)

    assert response is not None
    assert len(response) > 0


if __name__ == "__main__":
    test_llm()