# app/routes/dams.py

from flask import Blueprint, jsonify, abort
from ..models import Dam
from .. import db

dams_bp = Blueprint('dams_bp', __name__, url_prefix='/api/dams')

@dams_bp.route('/', methods=['GET'])
def get_dams():
    dams = Dam.query.all()
    return jsonify([{
        'dam_id': dam.dam_id,
        'dam_name': dam.dam_name,
        'full_volume': dam.full_volume,
        'latitude': float(dam.latitude) if dam.latitude else None,
        'longitude': float(dam.longitude) if dam.longitude else None
    } for dam in dams])

@dams_bp.route('/<string:dam_id>', methods=['GET'])
def get_dam(dam_id):
    dam = Dam.query.get(dam_id)
    if not dam:
        abort(404, description="Dam not found.")
    return jsonify({
        'dam_id': dam.dam_id,
        'dam_name': dam.dam_name,
        'full_volume': dam.full_volume,
        'latitude': float(dam.latitude) if dam.latitude else None,
        'longitude': float(dam.longitude) if dam.longitude else None
    })
