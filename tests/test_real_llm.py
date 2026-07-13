import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.llm import HuggingFaceLLM

llm = HuggingFaceLLM()

print("=" * 60)

response = llm.invoke(
    "Explain emergency fund in one sentence."
)

print(response)

print("=" * 60)