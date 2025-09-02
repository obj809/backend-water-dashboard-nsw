# app/routes/dam_groups.py

from flask_restx import Namespace, Resource, fields
from ..models import DamGroup
from ..utils.db import get_or_404

dam_groups_bp = Namespace('DamGroups', description='Endpoints for managing dam groups')

group_model = dam_groups_bp.model('Group', {
    'group_name': fields.String(required=True, description='The name of the group'),
})

@dam_groups_bp.route('/', endpoint='dam_groups_list')
class GroupsList(Resource):
    @dam_groups_bp.doc('list_dam_groups')
    @dam_groups_bp.marshal_list_with(group_model)
    def get(self):
        return DamGroup.query.all()

@dam_groups_bp.route('/<string:group_name>', endpoint='dam_groups_detail')
@dam_groups_bp.param('group_name', 'The name of the group')
class Group(Resource):
    @dam_groups_bp.doc('get_dam_group')
    @dam_groups_bp.marshal_with(group_model)
    def get(self, group_name):
        return get_or_404(DamGroup, group_name, "Dam group not found.")
