# scripts/insert_dam_analysis_data.py

import os
import logging
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from datetime import date

# Load environment variables from the .env file
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

# Fetch database URI from environment variables
database_uri = os.getenv("SQLALCHEMY_DATABASE_URI")

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger()

def insert_dam_analysis_data():
    try:
        # Create SQLAlchemy engine
        engine = create_engine(database_uri)
        
        # Connect to the database
        with engine.connect() as connection:
            logger.info("Database connection successful!")
            
            # Define the INSERT query
            insert_query = text("""
                INSERT INTO overall_dam_analysis (
                    analysis_date,
                    avg_storage_volume_12_months,
                    avg_storage_volume_5_years,
                    avg_storage_volume_20_years,
                    avg_percentage_full_12_months,
                    avg_percentage_full_5_years,
                    avg_percentage_full_20_years,
                    avg_storage_inflow_12_months,
                    avg_storage_inflow_5_years,
                    avg_storage_inflow_20_years,
                    avg_storage_release_12_months,
                    avg_storage_release_5_years,
                    avg_storage_release_20_years
                )
                VALUES (
                    :analysis_date,
                    :avg_storage_volume_12_months,
                    :avg_storage_volume_5_years,
                    :avg_storage_volume_20_years,
                    :avg_percentage_full_12_months,
                    :avg_percentage_full_5_years,
                    :avg_percentage_full_20_years,
                    :avg_storage_inflow_12_months,
                    :avg_storage_inflow_5_years,
                    :avg_storage_inflow_20_years,
                    :avg_storage_release_12_months,
                    :avg_storage_release_5_years,
                    :avg_storage_release_20_years
                )
            """)

            # Example data to insert
            dam_analysis_data = [
                {
                    "analysis_date": date(2023, 1, 1),
                    "avg_storage_volume_12_months": 10500.0,
                    "avg_storage_volume_5_years": 11000.0,
                    "avg_storage_volume_20_years": 11500.0,
                    "avg_percentage_full_12_months": 95.0,
                    "avg_percentage_full_5_years": 93.5,
                    "avg_percentage_full_20_years": 92.0,
                    "avg_storage_inflow_12_months": 500.5,
                    "avg_storage_inflow_5_years": 510.5,
                    "avg_storage_inflow_20_years": 520.5,
                    "avg_storage_release_12_months": 300.3,
                    "avg_storage_release_5_years": 310.3,
                    "avg_storage_release_20_years": 320.3
                },
                {
                    "analysis_date": date(2023, 2, 1),
                    "avg_storage_volume_12_months": 11000.0,
                    "avg_storage_volume_5_years": 11500.0,
                    "avg_storage_volume_20_years": 12000.0,
                    "avg_percentage_full_12_months": 96.0,
                    "avg_percentage_full_5_years": 94.5,
                    "avg_percentage_full_20_years": 93.5,
                    "avg_storage_inflow_12_months": 510.5,
                    "avg_storage_inflow_5_years": 520.5,
                    "avg_storage_inflow_20_years": 530.5,
                    "avg_storage_release_12_months": 310.3,
                    "avg_storage_release_5_years": 320.3,
                    "avg_storage_release_20_years": 330.3
                }
            ]
            
            # Execute the INSERT queries using explicit parameter passing
            for data in dam_analysis_data:
                # Pass parameters as a dictionary to the execute method
                connection.execute(insert_query, data)
                logger.info(f"Inserted data for {data['analysis_date']} into overall_dam_analysis table")

            # Commit the transaction (this is implicit when using context manager with engine.connect())
            logger.info("Data successfully inserted into the database.")

    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    insert_dam_analysis_data()
