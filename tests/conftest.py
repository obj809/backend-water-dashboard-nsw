# tests/conftest.py
import os
import sys
import importlib
import pytest
from datetime import date

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

TEST_DB_URI = "sqlite:///:memory:"

@pytest.fixture(scope="session")
def app():
    os.environ["SQLALCHEMY_DATABASE_URI"] = TEST_DB_URI
    os.environ["DEBUG"] = "False"

    import app.config as app_config
    importlib.reload(app_config)

    app_config.Config.SQLALCHEMY_DATABASE_URI = TEST_DB_URI
    app_config.Config.DEBUG = False

    from app import create_app, db as _db

    app = create_app()
    app.testing = True

    with app.app_context():
        _db.create_all()
        yield app
        _db.session.remove()
        _db.drop_all()


@pytest.fixture(scope="session")
def client(app):
    return app.test_client()


@pytest.fixture()
def db(app):
    from app import db as _db
    return _db


@pytest.fixture()
def reset_db(app):
    from app import db as _db
    with app.app_context():
        _db.session.remove()
        _db.drop_all()
        _db.create_all()
        yield
        _db.session.remove()


@pytest.fixture()
def seed_minimal(reset_db, db):
    from app.models import (
        Dam, LatestData, DamResource, SpecificDamAnalysis,
        OverallDamAnalysis, DamGroup, DamGroupMember
    )

    dam = Dam(dam_id="WORONOR", dam_name="Woronora", full_volume=1000, latitude=-34.04, longitude=150.999999)
    db.session.add(dam)

    latest = LatestData(
        dam_id="WORONOR", dam_name="Woronora", date=date(2025, 8, 1),
        storage_volume=500.123, percentage_full=50.12, storage_inflow=2.345, storage_release=1.234
    )
    db.session.add(latest)

    res1 = DamResource(dam_id="WORONOR", date=date(2025, 7, 31),
                       storage_volume=499.111, percentage_full=49.91, storage_inflow=1.111, storage_release=0.999)
    res2 = DamResource(dam_id="WORONOR", date=date(2025, 8, 1),
                       storage_volume=500.222, percentage_full=50.02, storage_inflow=2.222, storage_release=1.111)
    db.session.add_all([res1, res2])

    spec = SpecificDamAnalysis(
        dam_id="WORONOR", analysis_date=date(2025, 8, 1),
        avg_storage_volume_12_months=480.000, avg_storage_volume_5_years=470.000, avg_storage_volume_20_years=460.000,
        avg_percentage_full_12_months=48.00, avg_percentage_full_5_years=47.00, avg_percentage_full_20_years=46.00,
        avg_storage_inflow_12_months=1.2, avg_storage_inflow_5_years=1.1, avg_storage_inflow_20_years=1.0,
        avg_storage_release_12_months=1.0, avg_storage_release_5_years=0.9, avg_storage_release_20_years=0.8
    )
    db.session.add(spec)

    overall = OverallDamAnalysis(
        analysis_date=date(2025, 8, 1),
        avg_storage_volume_12_months=480.000, avg_storage_volume_5_years=470.000, avg_storage_volume_20_years=460.000,
        avg_percentage_full_12_months=48.00, avg_percentage_full_5_years=47.00, avg_percentage_full_20_years=46.00,
        avg_storage_inflow_12_months=1.2, avg_storage_inflow_5_years=1.1, avg_storage_inflow_20_years=1.0,
        avg_storage_release_12_months=1.0, avg_storage_release_5_years=0.9, avg_storage_release_20_years=0.8
    )
    db.session.add(overall)

    group = DamGroup(group_name="Sydney")
    db.session.add(group)
    db.session.add(DamGroupMember(group_name="Sydney", dam_id="WORONOR"))

    db.session.commit()
