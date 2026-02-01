# app/__init__.py
from __future__ import annotations

import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api

from .config import Config

db = SQLAlchemy()
migrate = Migrate()


def _get_cors_origins() -> list[str]:
    """
    Read allowed CORS origins from the CORS_ORIGINS env var.

    Example:
      CORS_ORIGINS=https://frontend-water-dashboard-nsw.netlify.app,http://localhost:5173

    Notes:
    - Origins should NOT include trailing slashes.
    - Comma-separated list.
    """
    raw = os.getenv("CORS_ORIGINS", "").strip()

    origins = [o.strip().rstrip("/") for o in raw.split(",") if o.strip()]

    if not origins:
        raise RuntimeError(
            "CORS_ORIGINS environment variable must be set to a comma-separated list of origins "
            "(e.g. https://frontend-water-dashboard-nsw.netlify.app,http://localhost:5173)"
        )

    return origins


def create_app() -> Flask:
    app = Flask(__name__)

    # Load + validate config from environment
    Config.refresh_from_env()
    Config.validate()
    app.config.from_object(Config)

    # Optional: minimal, redacted debug output
    if getattr(Config, "DEBUG", False):
        uri = app.config.get("SQLALCHEMY_DATABASE_URI") or ""
        print(f"DEBUG (Config): Using {getattr(Config, 'DB_PROVIDER', 'unknown')} database")
        if uri:
            print("DEBUG (create_app): SQLALCHEMY_DATABASE_URI loaded (redacted):", uri[:30] + "...")

    # CORS: env-driven allowed origins
    allowed_origins = _get_cors_origins()
    if getattr(Config, "DEBUG", False):
        print("DEBUG (CORS): Allowed origins:", allowed_origins)

    CORS(
        app,
        resources={r"/api/*": {"origins": allowed_origins}},
    )

    # Init extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Error handling
    from .errors import register_error_handlers
    register_error_handlers(app)

    # API docs (Swagger UI)
    api = Api(
        app,
        version="1.0",
        title="Dam Management API",
        description="API documentation for Dam Management System",
        doc="/api/docs",
    )

    # Namespaces
    from .routes.main import main_bp
    from .routes.dams import dams_bp
    from .routes.latest_data import latest_data_bp
    from .routes.dam_resources import dam_resources_bp
    from .routes.specific_dam_analysis import specific_dam_analysis_bp
    from .routes.overall_dam_analysis import overall_dam_analysis_bp
    from .routes.dam_groups import dam_groups_bp
    from .routes.dam_group_members import dam_group_members_bp

    api.add_namespace(main_bp, path="/api")
    api.add_namespace(dams_bp, path="/api/dams")
    api.add_namespace(latest_data_bp, path="/api/latest_data")
    api.add_namespace(dam_resources_bp, path="/api/dam_resources")
    api.add_namespace(specific_dam_analysis_bp, path="/api/specific_dam_analysis")
    api.add_namespace(overall_dam_analysis_bp, path="/api/overall_dam_analysis")
    api.add_namespace(dam_groups_bp, path="/api/dam_groups")
    api.add_namespace(dam_group_members_bp, path="/api/dam_group_members")

    return app