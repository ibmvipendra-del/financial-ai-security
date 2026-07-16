from datetime import datetime
import json
from pathlib import Path


class AuditLogger:

    def __init__(self):

        self.log_dir = Path("logs")
        self.log_dir.mkdir(exist_ok=True)

        self.log_file = self.log_dir / "audit_log.jsonl"

    def log(self, event: dict):

        event["timestamp"] = datetime.utcnow().isoformat()

        with open(self.log_file, "a", encoding="utf-8") as f:

            f.write(json.dumps(event, default=str))

            f.write("\n")