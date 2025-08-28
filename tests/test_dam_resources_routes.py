# tests/test_dam_resources_routes.py

def test_resources_list_paginated(client, seed_minimal):
    r = client.get("/api/dam_resources/?per_page=1")
    assert r.status_code == 200
    j = r.get_json()
    assert j["meta"]["per_page"] == 1
    assert "next" in j["links"]

def test_resource_detail_found(client, seed_minimal):
    # First list to discover resource_id
    j = client.get("/api/dam_resources/").get_json()
    rid = j["data"][0]["resource_id"]
    assert client.get(f"/api/dam_resources/{rid}").status_code == 200
