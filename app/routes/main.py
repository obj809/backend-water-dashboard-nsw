# app/routes/main.py

from flask import Blueprint

# Define the Blueprint with a unique name
main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def home():
    return "Welcome to your Flask App!"