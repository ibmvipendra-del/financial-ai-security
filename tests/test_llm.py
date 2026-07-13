import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.llm import LLMService


llm = LLMService()

response = llm.invoke(
    "Explain emergency fund in one paragraph."
)

print(response)