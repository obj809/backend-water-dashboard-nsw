# tests/test_utils_dates.py

import pytest
from app.utils.dates import parse_iso_date

def test_parse_iso_date_ok():
    d = parse_iso_date("2025-08-01")
    assert d.year == 2025 and d.month == 8 and d.day == 1

def test_parse_iso_date_bad():
    with pytest.raises(Exception):  # BadRequest
        parse_iso_date("2025-13-99")
