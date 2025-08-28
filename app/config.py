# app/config.py
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    DEBUG = os.getenv('DEBUG', 'True') == 'True'
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')  # initial value is fine
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @classmethod
    def refresh_from_env(cls):
        """Re-read env vars so tests (and runtime) can override between imports."""
        cls.DEBUG = os.getenv('DEBUG', 'True') == 'True'
        cls.SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

    @classmethod
    def validate(cls):
        # 🔑 ensure we re-sync with current environment before validating
        cls.refresh_from_env()
        print("DEBUG (Config): SQLALCHEMY_DATABASE_URI loaded:", cls.SQLALCHEMY_DATABASE_URI)
        if not cls.SQLALCHEMY_DATABASE_URI:
            raise ValueError(
                "SQLALCHEMY_DATABASE_URI is not set. Ensure it's defined in the .env file "
                "or as an environment variable. Check the .env file's location and syntax."
            )
