import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.graph import graph


print("=" * 60)
print("Emergency Fund Test")
print("=" * 60)

response = graph.invoke(
    {
        "question": "My monthly expense is 80000. How much emergency fund should I keep?"
    }
)

print(response["answer"])


print("\n" + "=" * 60)
print("General Chat Test")
print("=" * 60)

response = graph.invoke(
    {
        "question": "Hello"
    }
)

print(response["answer"])