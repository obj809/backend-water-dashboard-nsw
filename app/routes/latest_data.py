# app/routes/latest_data.py

from flask import Blueprint, jsonify, abort
from ..models import LatestData
from .. import db

latest_data_bp = Blueprint('latest_data_bp', __name__, url_prefix='/api/latest_data')

@latest_data_bp.route('/', methods=['GET'])
def get_latest_data():
    data_entries = LatestData.query.all()
    return jsonify([{
        'dam_id': entry.dam_id,
        'dam_name': entry.dam_name,
        'date': entry.date.isoformat(),
        'storage_volume': float(entry.storage_volume) if entry.storage_volume else None,
        'percentage_full': float(entry.percentage_full) if entry.percentage_full else None,
        'storage_inflow': float(entry.storage_inflow) if entry.storage_inflow else None,
        'storage_release': float(entry.storage_release) if entry.storage_release else None
    } for entry in data_entries])

@latest_data_bp.route('/<string:dam_id>', methods=['GET'])
def get_latest_data_by_dam(dam_id):
    data = LatestData.query.get(dam_id)
    if not data:
        abort(404, description="Latest data for the specified dam not found.")
    return jsonify({
        'dam_id': data.dam_id,
        'dam_name': data.dam_name,
        'date': data.date.isoformat(),
        'storage_volume': float(data.storage_volume) if data.storage_volume else None,
        'percentage_full': float(data.percentage_full) if data.percentage_full else None,
        'storage_inflow': float(data.storage_inflow) if data.storage_inflow else None,
        'storage_release': float(data.storage_release) if data.storage_release else None
    })
