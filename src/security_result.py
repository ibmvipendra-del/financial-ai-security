from dataclasses import dataclass
from typing import List


@dataclass
class SecurityResult:
    safe: bool
    score: int
    risk: str

    recommendation: str
    confidence: float

    attack_types: List[str]

    owasp: List[str]

    mitre: List[str]

    detector_results: dict