# app/routes/dam_groups.py

from flask import Blueprint, jsonify, abort
from ..models import DamGroup
from .. import db

dam_groups_bp = Blueprint('dam_groups_bp', __name__, url_prefix='/api/dam_groups')

@dam_groups_bp.route('/', methods=['GET'])
def get_dam_groups():
    groups = DamGroup.query.all()
    return jsonify([{
        'group_name': group.group_name
    } for group in groups])

@dam_groups_bp.route('/<string:group_name>', methods=['GET'])
def get_dam_group(group_name):
    group = DamGroup.query.get(group_name)
    if not group:
        abort(404, description="Dam group not found.")
    return jsonify({
        'group_name': group.group_name
    })
