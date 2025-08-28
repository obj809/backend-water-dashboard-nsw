# tests/factories.py

from datetime import date
from app.models import Dam, DamResource

def make_dam(i):
    return Dam(dam_id=f"DAM{i}", dam_name=f"Dam {i}", full_volume=1000+i, latitude=-33.0-i, longitude=151.0+i)

def make_resource(dam_id, d, v=400.0):
    return DamResource(dam_id=dam_id, date=d, storage_volume=v, percentage_full=40.0, storage_inflow=1.0, storage_release=1.0)
