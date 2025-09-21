# tests/test_empty_db_edge_cases.py

def _assert_error_payload(data, expected_codes=(404, 400), contains_any=None):
    if "error" in data:
        code = data["error"].get("code")
        if code is not None:
            assert code in expected_codes
        msg = str(data["error"].get("message", ""))
    elif "message" in data:
        msg = str(data["message"])
    else:
        raise AssertionError(f"Unexpected error JSON: {data}")

    if contains_any:
        m = msg.lower()
        assert any(sub.lower() in m for sub in contains_any), \
            f"Expected one of {contains_any} in '{msg}'"


def test_detail_endpoints_404_when_no_data(client, reset_db):
    candidates = [
        "/api/dams/NOPE",
        "/api/latest_data/NOPE",
        "/api/dam_resources/1",
        "/api/specific_dam_analysis/NOPE",
        "/api/specific_dam_analysis/NOPE/2025-08-01",
        "/api/overall_dam_analysis/2025-08-01",
        "/api/dam_groups/Nowhere",
        "/api/dam_group_members/Nowhere",
    ]
    for url in candidates:
        r = client.get(url)
        assert r.status_code in (404, 400)
        data = r.get_json()
        _assert_error_payload(
            data,
            expected_codes=(404, 400),
            contains_any=("not found", "no", "missing", "invalid", "members")
        )


def test_overall_detail_bad_date_still_400_with_empty_db(client, reset_db):
    r = client.get("/api/overall_dam_analysis/2025-99-99")
    assert r.status_code == 400
    data = r.get_json()
    _assert_error_payload(data, expected_codes=(400,), contains_any=("invalid date", "invalid"))
