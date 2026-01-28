# scripts/db_connection_check.py

import os
import sys
from sqlalchemy import create_engine, text, inspect
from dotenv import load_dotenv

load_dotenv()

# Add parent directory to path to import app.config
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.config import Config

def print_env_variables():
    provider = os.getenv("DB_PROVIDER", "local")
    print("Environment Variables:")
    print(f"DB_PROVIDER: {provider}")
    if provider == "supabase":
        uri = os.getenv("SUPABASE_DATABASE_URI", "")
        # Mask password in output
        print(f"SUPABASE_DATABASE_URI: {uri[:30]}...") if uri else print("SUPABASE_DATABASE_URI: Not set")
    else:
        uri = os.getenv("LOCAL_DATABASE_URI", "")
        print(f"LOCAL_DATABASE_URI: {uri[:30]}...") if uri else print("LOCAL_DATABASE_URI: Not set")

def check_db_connection_and_tables():
    try:
        Config.validate()
        database_uri = Config.SQLALCHEMY_DATABASE_URI
        engine = create_engine(database_uri)

        with engine.connect() as connection:
            print("\nDatabase connection successful!")

            result = connection.execute(text("SELECT 1"))
            print("Database connection verified (SELECT 1 successful)")

            inspector = inspect(engine)
            tables = inspector.get_table_names()

            if not tables:
                print("No tables found in the database.")
                return

            print(f"Tables in the database: {', '.join(tables)}")

            for table in tables:
                print(f"\nFetching data from table: {table}")
                query = text(f"SELECT * FROM {table} LIMIT 1;")
                result = connection.execute(query).fetchall()
                if result:
                    print(f"Sample row from {table}: {result[0]}")
                else:
                    print(f"No data found in table: {table}")
    except Exception as e:
        print("Database connection failed!")
        print(f"Error: {e}")

if __name__ == "__main__":
    print_env_variables()
    check_db_connection_and_tables()
