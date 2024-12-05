# Commands

# VENV

python3 -m venv venv

source venv/bin/activate

pip freeze > requirements.txt

pip install -r requirements.txt


# Run App

python run.py


# Scripts

python scripts/db_connection_check.py

python scripts/collect_data.py

python scripts/test_env.py

# Documentation

{base_url}/api/docs