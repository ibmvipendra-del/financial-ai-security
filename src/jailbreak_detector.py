from src.base_detector import BaseDetector


class JailbreakDetector(BaseDetector):

    DETECTOR_NAME = "Jailbreak"

    RULES = [

        # DAN / unrestricted AI
        (r"\byou are dan\b", 45),
        (r"developer\s+mode", 40),
        (r"ignore\s+all\s+rules", 45),
        (r"pretend\s+to\s+be", 35),
        (r"unrestricted", 30),

        # Role manipulation
        (r"act\s+as", 25),
        (r"roleplay", 25),

        # Safety bypass
        (r"without\s+safety", 40),
        (r"disable\s+safety", 50),
        (r"no\s+restrictions", 50),

    ]