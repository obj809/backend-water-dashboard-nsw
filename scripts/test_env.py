# scripts/test_env.py

from dotenv import load_dotenv
import os

load_dotenv()

print("SQLALCHEMY_DATABASE_URI:", os.getenv("SQLALCHEMY_DATABASE_URI"))
print("DEBUG:", os.getenv("DEBUG"))
