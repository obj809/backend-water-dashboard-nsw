# tests/test_utils_pagination.py

from app.utils.pagination import get_pagination_params

def test_get_pagination_params_clamps(client, monkeypatch):
    with client.application.test_request_context("/?page=0&per_page=999999"):
        page, per_page = get_pagination_params()
        assert page == 1
        assert per_page <= 200  # MAX_PER_PAGE
