# app/__init__.py
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Validate configuration
    Config.validate()

    # Debugging: Print SQLALCHEMY_DATABASE_URI in app config
    print("DEBUG (create_app): SQLALCHEMY_DATABASE_URI in config:", app.config.get("SQLALCHEMY_DATABASE_URI"))

    CORS(app)
    db.init_app(app)

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
