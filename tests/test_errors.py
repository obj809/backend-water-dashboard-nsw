# tests/test_errors.py

def test_404_json_shape(client):
    resp = client.get("/api/unknown")
    assert resp.status_code == 404
    data = resp.get_json()
    assert "error" in data and "code" in data["error"]
