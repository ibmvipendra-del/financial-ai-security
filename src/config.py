from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_PATH = BASE_DIR / "database" / "finance.db"

APP_NAME = "Financial AI Security Platform"

DEBUG = True

HF_TOKEN = os.getenv("HF_TOKEN")

# Development model (works on CPU)
MODEL_NAME = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

TEMPERATURE = 0.2

MAX_NEW_TOKENS = 32