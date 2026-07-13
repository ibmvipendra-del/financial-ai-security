import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.prompts import financial_prompt

prompt = financial_prompt.invoke(
    {
        "question": "How much emergency fund should I keep?"
    }
)

print("=" * 60)

for msg in prompt.messages:
    print(f"{msg.type.upper()}:")
    print(msg.content)
    print()

print("=" * 60)