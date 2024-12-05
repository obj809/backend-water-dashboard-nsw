# app/__init__.py

from flask import Flask

def create_app():
    app = Flask(__name__)

    # Example: Load config from a file or environment variables
    app.config.from_object('app.config.Config')

    # Register blueprints or routes
    with app.app_context():
        from .routes import main
        app.register_blueprint(main)

    return app
