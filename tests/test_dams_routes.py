# tests/test_dams_routes.py

def test_list_dams_pagination(client, db, seed_minimal):
    r = client.get("/api/dams/?page=1&per_page=1")
    assert r.status_code == 200
    payload = r.get_json()
    assert "data" in payload and "meta" in payload and "links" in payload
    assert payload["meta"]["per_page"] == 1

def test_get_dam_detail_found(client, seed_minimal):
    r = client.get("/api/dams/WORONOR")
    assert r.status_code == 200
    assert r.get_json()["dam_id"] == "WORONOR"

def test_get_dam_detail_404(client):
    r = client.get("/api/dams/NOPE")
    assert r.status_code == 404
