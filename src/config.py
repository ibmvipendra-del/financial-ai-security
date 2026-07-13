from pathlib import Path
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Project Root
BASE_DIR = Path(__file__).resolve().parent.parent

# Database
DATABASE_PATH = BASE_DIR / "database" / "finance.db"

# Application
APP_NAME = "Financial AI Security Platform"
DEBUG = True

# Hugging Face
HF_TOKEN = os.getenv("HF_TOKEN")

MODEL_NAME = "Qwen/Qwen2.5-3B-Instruct"
TEMPERATURE = 0.3
MAX_NEW_TOKENS = 512