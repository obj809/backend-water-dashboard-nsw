# tests/test_main_route.py

def test_main_welcome_message(client, reset_db):
    r = client.get("/api/")
    assert r.status_code == 200
    data = r.get_json()
    assert isinstance(data, dict)
    assert data.get("message") == "Welcome to the Dam Management API!"
