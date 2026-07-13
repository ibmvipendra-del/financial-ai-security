from datetime import datetime
from pathlib import Path
import json


class AuditLogger:

    def __init__(self):

        self.log_dir = Path("logs")

        self.log_dir.mkdir(exist_ok=True)

        self.log_file = self.log_dir / "audit.log"

    def log(
        self,
        question: str,
        plan: dict,
        answer: str,
        risk: str = "LOW",
    ):

        event = {

            "timestamp": datetime.utcnow().isoformat(),

            "question": question,

            "plan": plan,

            "answer": answer,

            "risk": risk,

        }

        with open(
            self.log_file,
            "a",
            encoding="utf-8"
        ) as f:

            f.write(
                json.dumps(event)
            )

            f.write("\n")