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

MODEL_NAME = "mistralai/Mistral-7B-Instruct-v0.3"

TEMPERATURE = 0.2

MAX_NEW_TOKENS = 512