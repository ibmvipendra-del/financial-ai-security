from pathlib import Path
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Project Root
BASE_DIR = Path(__file__).resolve().parent

# Database
DATABASE_PATH = BASE_DIR / "database" / "finance.db"

# Model Configuration
MODEL_NAME = "Qwen/Qwen2.5-3B-Instruct"
TEMPERATURE = 0.3
MAX_NEW_TOKENS = 512

# Application
APP_NAME = "Financial AI Security Platform"
DEBUG = True
