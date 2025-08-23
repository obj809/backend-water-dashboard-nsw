# app/utils/dates.py
from datetime import date
def parse_iso_date(s: str) -> date:
    try:
        return date.fromisoformat(s)
    except Exception:
        from werkzeug.exceptions import BadRequest
        raise BadRequest("Invalid date format. Use YYYY-MM-DD.")
