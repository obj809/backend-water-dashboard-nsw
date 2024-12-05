# app/__init__.py

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Validate configuration
    Config.validate()

    # Debugging: Print SQLALCHEMY_DATABASE_URI in app config
    print("DEBUG (create_app): SQLALCHEMY_DATABASE_URI in config:", app.config.get("SQLALCHEMY_DATABASE_URI"))

    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from .routes import main_bp, dams_bp, latest_data_bp, dam_resources_bp, specific_dam_analysis_bp, overall_dam_analysis_bp, dam_groups_bp, dam_group_members_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(dams_bp)
    app.register_blueprint(latest_data_bp)
    app.register_blueprint(dam_resources_bp)
    app.register_blueprint(specific_dam_analysis_bp)
    app.register_blueprint(overall_dam_analysis_bp)
    app.register_blueprint(dam_groups_bp)
    app.register_blueprint(dam_group_members_bp)

    return app

