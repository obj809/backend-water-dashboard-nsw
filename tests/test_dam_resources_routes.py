# tests/test_dam_resources_routes.py

def test_resources_list_plain(client, seed_minimal):
    r = client.get("/api/dam_resources/")
    assert r.status_code == 200
    data = r.get_json()
    assert isinstance(data, list)
    assert len(data) >= 1
    assert "resource_id" in data[0]

def test_resource_detail_found(client, seed_minimal):
    data = client.get("/api/dam_resources/").get_json()
    rid = data[0]["resource_id"]
    assert client.get(f"/api/dam_resources/{rid}").status_code == 200
