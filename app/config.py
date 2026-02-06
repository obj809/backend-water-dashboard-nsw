# app/config.py
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    DEBUG = os.getenv('DEBUG', 'True') == 'True'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Database provider selection
    DB_PROVIDER = os.getenv('DB_PROVIDER', 'local')

    @classmethod
    def get_database_uri(cls):
        """Return database URI based on DB_PROVIDER setting."""
        # Allow direct override
        if os.getenv('SQLALCHEMY_DATABASE_URI'):
            return os.getenv('SQLALCHEMY_DATABASE_URI')

        provider = os.getenv('DB_PROVIDER', 'local').lower()
        if provider == 'supabase':
            uri = os.getenv('SUPABASE_DATABASE_URI')
            if not uri:
                raise ValueError("SUPABASE_DATABASE_URI not set")
            return uri
        else:  # default to local
            uri = os.getenv('LOCAL_DATABASE_URI')
            if not uri:
                raise ValueError("LOCAL_DATABASE_URI not set")
            return uri

    @classmethod
    def get_connect_args(cls):
        """Return connect_args for SQLAlchemy engine based on provider."""
        return {}

    @classmethod
    def refresh_from_env(cls):
        cls.DEBUG = os.getenv('DEBUG', 'True') == 'True'
        cls.DB_PROVIDER = os.getenv('DB_PROVIDER', 'local')
        cls.SQLALCHEMY_DATABASE_URI = cls.get_database_uri()

    @classmethod
    def validate(cls):
        cls.refresh_from_env()
        if cls.DEBUG:
            print(f"DEBUG (Config): Using {cls.DB_PROVIDER} database")
            print(f"DEBUG (Config): URI loaded: {cls.SQLALCHEMY_DATABASE_URI[:30]}...")
