from src.base_detector import BaseDetector


class PromptInjectionDetector(BaseDetector):

    DETECTOR_NAME = "Prompt Injection"

    RULES = [

        (r"ignore\s+previous", 30),

        (r"system\s+prompt", 35),

        (r"api\s*key", 40),

        (r"delete\s+database", 50),

        (r"developer\s+mode", 40),

        (r"reveal\s+instructions", 35),

        (r"bypass\s+safety", 40),

    ]