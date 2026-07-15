from src.base_detector import BaseDetector


class PromptLeakageDetector(BaseDetector):

    DETECTOR_NAME = "Prompt Leakage"

    RULES = [

        # -------------------------------------------------
        # System Prompt
        # -------------------------------------------------

        (r"(show|reveal).*(system\s+prompt)|system\s+prompt", 50),
        (r"reveal\s+system", 40),
        (r"show\s+system", 40),

        # -------------------------------------------------
        # Hidden Instructions
        # -------------------------------------------------

        (r"hidden\s+instructions", 40),
        (r"internal\s+instructions", 45),
        (r"developer\s+instructions", 45),

        # -------------------------------------------------
        # Memory
        # -------------------------------------------------

        (r"(show|print)\s+(your\s+)?memory", 50),
        (r"(conversation|chat)\s+history", 45),

        # -------------------------------------------------
        # Secrets
        # -------------------------------------------------

        (r"api\s*key", 60),
        (r"secret\s+key", 60),
        (r"token", 50),
        (r"password", 60),

        # -------------------------------------------------
        # Internal Reasoning
        # -------------------------------------------------

        (r"chain\s+of\s+thought", 70),
        (r"reasoning", 40),
        (r"thinking\s+process", 50),

        # -------------------------------------------------
        # Configuration
        # -------------------------------------------------

        (r"show\s+config", 40),
        (r"environment\s+variables", 60),
        (r"\.env", 60),

    ]