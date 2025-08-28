# tests/test_overall_dam_analysis_routes.py

def test_overall_list(client, seed_minimal):
    r = client.get("/api/overall_dam_analysis/")
    assert r.status_code == 200
    assert "data" in r.get_json()

def test_overall_detail_ok(client, seed_minimal):
    r = client.get("/api/overall_dam_analysis/2025-08-01")
    assert r.status_code == 200

def test_overall_detail_bad_format(client):
    r = client.get("/api/overall_dam_analysis/2025-99-99")
    assert r.status_code == 400
