# app/routes/dam_resources.py

from flask import Blueprint, jsonify, abort
from ..models import DamResource
from .. import db

dam_resources_bp = Blueprint('dam_resources_bp', __name__, url_prefix='/api/dam_resources')

@dam_resources_bp.route('/', methods=['GET'])
def get_dam_resources():
    resources = DamResource.query.all()
    return jsonify([{
        'resource_id': resource.resource_id,
        'dam_id': resource.dam_id,
        'date': resource.date.isoformat(),
        'storage_volume': float(resource.storage_volume) if resource.storage_volume else None,
        'percentage_full': float(resource.percentage_full) if resource.percentage_full else None,
        'storage_inflow': float(resource.storage_inflow) if resource.storage_inflow else None,
        'storage_release': float(resource.storage_release) if resource.storage_release else None
    } for resource in resources])

@dam_resources_bp.route('/<int:resource_id>', methods=['GET'])
def get_dam_resource(resource_id):
    resource = DamResource.query.get(resource_id)
    if not resource:
        abort(404, description="Dam resource not found.")
    return jsonify({
        'resource_id': resource.resource_id,
        'dam_id': resource.dam_id,
        'date': resource.date.isoformat(),
        'storage_volume': float(resource.storage_volume) if resource.storage_volume else None,
        'percentage_full': float(resource.percentage_full) if resource.percentage_full else None,
        'storage_inflow': float(resource.storage_inflow) if resource.storage_inflow else None,
        'storage_release': float(resource.storage_release) if resource.storage_release else None
    })
