# tests/test_dam_groups_routes.py

def test_groups_list(client, seed_minimal):
    assert client.get("/api/dam_groups/").status_code == 200

def test_group_detail(client, seed_minimal):
    r = client.get("/api/dam_groups/Sydney")
    assert r.status_code == 200
    assert r.get_json()["group_name"] == "Sydney"
