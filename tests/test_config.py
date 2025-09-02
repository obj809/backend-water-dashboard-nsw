# tests/test_config.py

import os
import importlib
import pytest

def test_config_validate_raises_when_missing(monkeypatch):
    monkeypatch.delenv("SQLALCHEMY_DATABASE_URI", raising=False)
    from app.config import Config
    with pytest.raises(ValueError):
        Config.validate()

def test_docs_mounts(client):
    resp = client.get("/api/docs")
    assert resp.status_code in (200, 301, 302)
