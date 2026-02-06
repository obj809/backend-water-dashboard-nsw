# tests/test_metadata_routes.py

def test_metadata_with_data(client, seed_minimal):
    """Test metadata endpoint returns the latest data date when data exists"""
    r = client.get("/api/metadata/")
    assert r.status_code == 200
    data = r.get_json()
    assert "latest_data_date" in data
    assert data["latest_data_date"] is not None
    # Should be in ISO format (YYYY-MM-DD)
    assert len(data["latest_data_date"]) == 10
    assert data["latest_data_date"].count("-") == 2

def test_metadata_empty_database(client, reset_db):
    """Test metadata endpoint when no data exists"""
    r = client.get("/api/metadata/")
    assert r.status_code == 200
    data = r.get_json()
    assert "latest_data_date" in data
    assert data["latest_data_date"] is None
