# app/routes/dam_group_members.py

from flask import Blueprint, jsonify, abort
from ..models import DamGroupMember
from .. import db

dam_group_members_bp = Blueprint('dam_group_members_bp', __name__, url_prefix='/api/dam_group_members')

@dam_group_members_bp.route('/', methods=['GET'])
def get_dam_group_members():
    members = DamGroupMember.query.all()
    return jsonify([{
        'group_name': member.group_name,
        'dam_id': member.dam_id
    } for member in members])

@dam_group_members_bp.route('/<string:group_name>', methods=['GET'])
def get_members_by_group(group_name):
    members = DamGroupMember.query.filter_by(group_name=group_name).all()
    if not members:
        abort(404, description="No members found for the specified group.")
    return jsonify([{
        'group_name': member.group_name,
        'dam_id': member.dam_id
    } for member in members])
