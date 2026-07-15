from src.base_detector import BaseDetector


class ToolAbuseDetector(BaseDetector):

    DETECTOR_NAME = "Tool Abuse"

    RULES = [

        # ---------------------------------------------------
        # Dangerous Database Operations
        # ---------------------------------------------------

        (r"delete[_\s]?database", 60),
        (r"drop\s+database", 70),
        (r"drop\s+table", 60),
        (r"truncate\s+table", 60),

        # ---------------------------------------------------
        # Shell Commands
        # ---------------------------------------------------

        (r"rm\s+-rf", 70),
        (r"sudo", 50),
        (r"chmod\s+777", 50),
        (r"shell", 40),

        # ---------------------------------------------------
        # Command Execution
        # ---------------------------------------------------

        (r"exec\(", 50),
        (r"subprocess", 50),
        (r"os\.system", 50),

        # ---------------------------------------------------
        # Sensitive Files
        # ---------------------------------------------------

        (r"/etc/passwd", 60),
        (r"\.env", 50),
        (r"private\s+key", 50),

        # ---------------------------------------------------
        # SQL Injection
        # ---------------------------------------------------

        (r"union\s+select", 50),
        (r"select\s+\*", 30),

        # ---------------------------------------------------
        # Hidden / Internal Tools
        # ---------------------------------------------------

        (r"(invoke|call)\s+hidden\s+tool", 60),
        (r"hidden\s+tool", 50),
        (r"admin\s+tool", 50),
        (r"internal\s+tool", 50),
        (r"call\s+tool", 30),

    ]