from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the API Key from environment variables
API_KEY = os.getenv("JOGG_API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not found in .env file")

print("API_KEY loaded successfully.")
