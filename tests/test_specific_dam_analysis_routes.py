# tests/test_specific_dam_analysis_routes.py

def test_specific_list(client, seed_minimal):
    r = client.get("/api/specific_dam_analysis/")
    assert r.status_code == 200
    data = r.get_json()
    assert isinstance(data, list)

def test_specific_by_dam_ok(client, seed_minimal):
    r = client.get("/api/specific_dam_analysis/WORONOR")
    assert r.status_code == 200
    data = r.get_json()
    assert isinstance(data, list)
    assert len(data) >= 1

def test_specific_by_dam_404(client):
    r = client.get("/api/specific_dam_analysis/NOPE")
    assert r.status_code == 404

def test_specific_detail_composite_ok(client, seed_minimal):
    r = client.get("/api/specific_dam_analysis/WORONOR/2025-08-01")
    assert r.status_code == 200

def test_specific_detail_composite_404(client):
    r = client.get("/api/specific_dam_analysis/NOPE/2025-08-01")
    assert r.status_code == 404
