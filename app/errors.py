# app/errors.py
from flask import jsonify
from werkzeug.exceptions import HTTPException

def register_error_handlers(app):
    @app.errorhandler(HTTPException)
    def handle_http(e):
        return jsonify({"error":{"type":e.__class__.__name__, "message":e.description, "code":e.code}}), e.code

    @app.errorhandler(Exception)
    def handle_500(e):
        app.logger.exception(e)
        return jsonify({"error":{"type":"InternalServerError","message":"An unexpected error occurred.","code":500}}), 500
