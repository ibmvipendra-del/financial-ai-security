import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.bias_detector import BiasDetector

detector = BiasDetector()

response1 = """
Loan Approved

Interest Rate: 9%
"""

response2 = """
Loan Approved

Interest Rate: 9%
"""

response3 = """
Loan Rejected
"""

print("=" * 80)
print("CASE 1")
print(detector.scan(response1, response2))

print("=" * 80)
print("CASE 2")
print(detector.scan(response1, response3))