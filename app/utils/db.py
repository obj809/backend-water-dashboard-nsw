# app/utils/db.py
from flask import abort
from .. import db

def get_or_404(model, pk, description="Resource not found."):
    """
    Wrapper around SQLAlchemy 2.x session.get() that raises a 404 if not found.

    - For simple PK models, pk is a scalar (e.g., "WORONOR").
    - For composite PK models, pk is a tuple in the declared PK order
      (e.g., ("WORONOR", date(2025, 8, 01))).
    """
    obj = db.session.get(model, pk)
    if obj is None:
        abort(404, description=description)
    return obj