# app/utils/db.py
from flask import abort
from .. import db

def get_or_404(model, pk, description="Resource not found."):
    obj = db.session.get(model, pk)
    if obj is None:
        abort(404, description=description)
    return obj