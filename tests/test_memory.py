import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.memory import ConversationMemory

memory = ConversationMemory()

memory.clear()

memory.add_message(
    "user",
    "My salary is ₹1,20,000."
)

memory.add_message(
    "assistant",
    "Thanks. I have saved your salary."
)

memory.add_message(
    "user",
    "My monthly expense is ₹60,000."
)

print("=" * 60)

for msg in memory.get_history():
    print(msg)

print("=" * 60)