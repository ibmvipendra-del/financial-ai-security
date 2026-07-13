import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.profile import UserProfile


profile = UserProfile()

profile.save_profile(
    name="Vipendra",
    age=37,
    income=120000,
    expense=60000,
    savings=1500000,
    goal="Financial Freedom",
)

print("=" * 60)

print(profile.get_profile())

print("=" * 60)