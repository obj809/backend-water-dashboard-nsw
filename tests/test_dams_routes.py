# tests/test_dams_routes.py

def test_list_dams_returns_list(client, db, seed_minimal):
    r = client.get("/api/dams/?page=1&per_page=1")
    assert r.status_code == 200
    data = r.get_json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert {"dam_id", "dam_name"}.issubset(data[0].keys())

def test_get_dam_detail_found(client, seed_minimal):
    r = client.get("/api/dams/WORONOR")
    assert r.status_code == 200
    assert r.get_json()["dam_id"] == "WORONOR"

def test_get_dam_detail_404(client):
    r = client.get("/api/dams/NOPE")
    assert r.status_code == 404
