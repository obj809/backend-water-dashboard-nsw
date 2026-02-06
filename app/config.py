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
        elif provider == 'oracle':
            user = os.getenv('ORACLE_DB_USER')
            password = os.getenv('ORACLE_DB_PASSWORD')
            dsn = os.getenv('ORACLE_DB_DSN')
            wallet_dir = os.getenv('ORACLE_WALLET_DIR')

            if not all([user, password, dsn]):
                raise ValueError("ORACLE_DB_USER, ORACLE_DB_PASSWORD, and ORACLE_DB_DSN must be set")

            # Set TNS_ADMIN for wallet location if provided
            if wallet_dir:
                os.environ['TNS_ADMIN'] = wallet_dir

            return f"oracle+oracledb://{user}:{password}@{dsn}"
        else:  # default to local
            uri = os.getenv('LOCAL_DATABASE_URI')
            if not uri:
                raise ValueError("LOCAL_DATABASE_URI not set")
            return uri

    @classmethod
    def get_connect_args(cls):
        """Return connect_args for SQLAlchemy engine based on provider."""
        provider = os.getenv('DB_PROVIDER', 'local').lower()
        if provider == 'oracle':
            wallet_dir = os.getenv('ORACLE_WALLET_DIR')
            wallet_password = os.getenv('ORACLE_WALLET_PASSWORD')

            if wallet_dir:
                connect_args = {
                    'config_dir': wallet_dir,
                    'wallet_location': wallet_dir,
                }
                if wallet_password:
                    connect_args['wallet_password'] = wallet_password
                return connect_args
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
