# scripts/test_env.py

from dotenv import load_dotenv
import os

load_dotenv()

# Check environment variables
print("SQLALCHEMY_DATABASE_URI:", os.getenv("SQLALCHEMY_DATABASE_URI"))
print("DEBUG:", os.getenv("DEBUG"))
