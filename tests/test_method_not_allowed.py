# tests/test_method_not_allowed.py
import pytest

# Endpoints that only define GET
LIST_ENDPOINTS = [
    "/api/dams/",
    "/api/latest_data/",
    "/api/dam_resources/",
    "/api/specific_dam_analysis/",
    "/api/overall_dam_analysis/",
    "/api/dam_groups/",
    "/api/dam_group_members/",
]
# Detail endpoints (use dummy IDs; existence isn't relevant for 405)
DETAIL_ENDPOINTS = [
    "/api/dams/ANY",
    "/api/latest_data/ANY",
    "/api/dam_resources/123",
    "/api/specific_dam_analysis/ANY",                # by-dam route
    "/api/specific_dam_analysis/ANY/2025-01-01",     # composite PK route
    "/api/overall_dam_analysis/2025-01-01",
    "/api/dam_groups/ANY",
    "/api/dam_group_members/ANY",
]

def _assert_error_payload(data, contains=None):
    """
    Accept either {"error": {..., "message": "...", "code": N}} from our
    global error handler OR {"message": "..."} from Flask-RESTX defaults.
    Optionally assert the message contains a substring.
    """
    if "error" in data:
        msg = str(data["error"].get("message", ""))
    elif "message" in data:
        msg = str(data["message"])
    else:
        raise AssertionError(f"Unexpected error JSON keys: {list(data.keys())}")
    if contains:
        assert contains.lower() in msg.lower(), f"Expected '{contains}' in '{msg}'"

@pytest.mark.parametrize("method", ["post", "put", "delete"])
@pytest.mark.parametrize("url", LIST_ENDPOINTS + DETAIL_ENDPOINTS)
def test_methods_not_allowed(client, reset_db, method, url):
    resp = getattr(client, method)(url, json={"x": 1})
    # Flask-RESTX returns 405 when a method is not implemented on a Resource
    assert resp.status_code == 405
    data = resp.get_json()
    _assert_error_payload(data, contains="not allowed")
