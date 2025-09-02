# tests/test_latest_data_routes.py

def test_latest_data_list(client, seed_minimal):
    r = client.get("/api/latest_data/")
    assert r.status_code == 200
    data = r.get_json()
    assert isinstance(data, list)
    assert len(data) >= 1

def test_latest_data_detail_found(client, seed_minimal):
    r = client.get("/api/latest_data/WORONOR")
    assert r.status_code == 200
    assert r.get_json()["dam_id"] == "WORONOR"

def test_latest_data_detail_404(client):
    r = client.get("/api/latest_data/NOPE")
    assert r.status_code == 404
