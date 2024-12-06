# app/routes/main.py

from flask_restx import Namespace, Resource

main_bp = Namespace('Main', description='Main route for the application')

@main_bp.route('/')
class Home(Resource):
    def get(self):
        """Welcome route"""
        return {"message": "Welcome to the Dam Management API!"}, 200
