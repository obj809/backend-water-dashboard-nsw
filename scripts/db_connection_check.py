# scripts/db_connection_check.py

import os
import sys
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

# Add parent directory to path to import app.config
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.config import Config

def check_db_connection():
    provider = os.getenv("DB_PROVIDER", "local")
    print(f"Checking {provider} database connection...")

    try:
        Config.validate()
        database_uri = Config.SQLALCHEMY_DATABASE_URI
        connect_args = Config.get_connect_args()

        engine = create_engine(database_uri, connect_args=connect_args)

        print("Attempting to connect...")
        with engine.connect() as connection:
            print("Executing test query...")
            connection.execute(text("SELECT 1"))
            print("✓ Database connection successful!")
    except Exception as e:
        print("✗ Database connection failed!")
        print(f"Error: {e}")

if __name__ == "__main__":
    check_db_connection()
