from dotenv import load_dotenv
import os

load_dotenv()  # Loads the .env file

WEBULL_USER = os.getenv("WEBULL_USER")
WEBULL_PASS = os.getenv("WEBULL_PASS")