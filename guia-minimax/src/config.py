import os
from dotenv import load_dotenv

load_dotenv()

MINIMAX_API_KEY = os.getenv("MINIMAX_API_KEY")
ANTHROPIC_BASE_URL = "https://api.minimax.io/anthropic"
OPENAI_BASE_URL = "https://api.minimax.io/v1"
DEFAULT_MODEL = "MiniMax-M3"
DEFAULT_MODEL_M2 = "MiniMax-M2.7"
