# scripts/collect_data.py

import os
import json
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from decimal import Decimal

# Load environment variables from .env file
load_dotenv()

# Fetch environment variables
database_uri = os.getenv("SQLALCHEMY_DATABASE_URI")

# Custom JSON encoder to handle Decimal objects
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)

def collect_and_save_data():
    try:
        # Create a SQLAlchemy engine
        engine = create_engine(database_uri)

        # Connect to the database
        with engine.connect() as connection:
            print("Database connection successful!")

            # Queries to fetch all data from the relevant tables
            queries = {
                "dams": "SELECT * FROM dams;",
                "dam_groups": "SELECT * FROM dam_groups;",
                "dam_group_members": "SELECT * FROM dam_group_members;"
            }

            results = {}

            # Execute each query and store the results
            for table_name, query in queries.items():
                print(f"Fetching data from table: {table_name}")
                result = connection.execute(text(query)).fetchall()
                
                # Convert SQLAlchemy row objects to dictionaries
                results[table_name] = [dict(row._mapping) for row in result] if result else []

            # Save results to a JSON file
            output_file = os.path.join(os.path.dirname(__file__), "collected_data.json")
            with open(output_file, "w") as f:
                json.dump(results, f, indent=4, cls=DecimalEncoder)

            print(f"Data successfully collected and saved to {output_file}")

    except Exception as e:
        print("An error occurred while collecting data!")
        print(f"Error: {e}")

if __name__ == "__main__":
    collect_and_save_data()
