# app/routes/dam_groups.py

from flask_restx import Namespace, Resource, fields
from ..models import DamGroup
from .. import db

dam_groups_bp = Namespace('DamGroups', description='Endpoints for managing dam groups')

# Define a model for dam groups
group_model = dam_groups_bp.model('Group', {
    'group_name': fields.String(required=True, description='The name of the group'),
})


@dam_groups_bp.route('/')
class GroupsList(Resource):
    @dam_groups_bp.doc('list_dam_groups')
    @dam_groups_bp.marshal_list_with(group_model)
    def get(self):
        """List all dam groups"""
        groups = DamGroup.query.all()
        return groups


@dam_groups_bp.route('/<string:group_name>')
@dam_groups_bp.param('group_name', 'The name of the group')
class Group(Resource):
    @dam_groups_bp.doc('get_dam_group')
    @dam_groups_bp.marshal_with(group_model)
    def get(self, group_name):
        """Get a dam group by name"""
        group = DamGroup.query.get(group_name)
        if not group:
            dam_groups_bp.abort(404, "Dam group not found.")
        return group
