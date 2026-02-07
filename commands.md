# Commands

# VENV

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt


# Run App

python run.py


# Scripts

python scripts/db_connection_check.py

python scripts/data_collection_and_export.py

python scripts/test_api_endpoints.py

python scripts/test_api_endpoints_preview.py

<!-- python scripts/insert_dam_analysis_data.py

python scripts/insert_specific_dam_analysis_data.py -->


# Documentation

{base_url}/api/docs

# Testing


pytest

pytest -v

pytest tests/test_config.py
pytest tests/test_errors.py
pytest tests/test_utils_dates.py
pytest tests/test_utils_pagination.py
pytest tests/test_utils_db.py
pytest tests/test_dams_routes.py
pytest tests/test_dam_resources_routes.py
pytest tests/test_latest_data_routes.py
pytest tests/test_overall_dam_analysis_routes.py
pytest tests/test_dam_groups_routes.py
pytest tests/test_dam_group_members_routes.py
pytest tests/test_specific_dam_analysis_routes.py


# Docker

# Local
docker compose up -d --build

# VPS
docker compose -f docker-compose.prod.yml up -d --build
