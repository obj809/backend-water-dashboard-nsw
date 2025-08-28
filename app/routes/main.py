# app/routes/main.py
from flask_restx import Namespace, Resource

main_bp = Namespace('Main', description='Main route for the application')

@main_bp.route('/', endpoint='main_home')
class Home(Resource):
    def get(self):
        return {"message": "Welcome to the Dam Management API!"}, 200
