import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
API_URL = os.getenv("GROQ_API_URL")
MODEL = os.getenv("GROQ_MODEL")

HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_URL = os.getenv("GEMINI_URL")

GEMINI_HEADERS = {"Content-Type": "application/json"}
