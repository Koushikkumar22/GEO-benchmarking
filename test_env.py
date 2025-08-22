import os
from dotenv import load_dotenv

load_dotenv()  # loads .env file

api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    print("✅ OpenAI API key loaded successfully!")
else:
    print("❌ API key not found. Check your .env file.")
