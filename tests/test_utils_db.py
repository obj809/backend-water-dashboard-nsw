# tests/test_utils_db.py

import pytest
from datetime import date
from app.utils.db import get_or_404
from app.models import Dam, SpecificDamAnalysis

def test_get_or_404_scalar_pk(app, db, seed_minimal):
    with app.app_context():
        obj = get_or_404(Dam, "WORONOR")
        assert obj.dam_name == "Woronora"

def test_get_or_404_composite_pk(app, db, seed_minimal):
    with app.app_context():
        obj = get_or_404(SpecificDamAnalysis, ("WORONOR", date(2025, 8, 1)))
        assert obj.dam_id == "WORONOR"

def test_get_or_404_not_found(app):
    from werkzeug.exceptions import NotFound
    with app.app_context():
        with pytest.raises(NotFound):
            get_or_404(Dam, "MISSING")
