# tests/test_dam_group_members_routes.py

def test_members_list(client, seed_minimal):
    assert client.get("/api/dam_group_members/").status_code == 200

def test_members_by_group_ok(client, seed_minimal):
    r = client.get("/api/dam_group_members/Sydney")
    assert r.status_code == 200
    assert len(r.get_json()["data"]) >= 1

def test_members_by_group_404(client):
    assert client.get("/api/dam_group_members/Nowhere").status_code == 404