# run.py
from dotenv import load_dotenv
import os

load_dotenv()
print("DEBUG (run.py): SQLALCHEMY_DATABASE_URI loaded:", os.getenv("SQLALCHEMY_DATABASE_URI"))

from app import create_app
from app.errors import register_error_handlers  # absolute import

app = create_app()
register_error_handlers(app)  # now app exists

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)
