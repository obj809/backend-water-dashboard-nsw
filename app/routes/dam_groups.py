# app/routes/dam_groups.py
#
# Adds pagination to:
#   - GET /api/dam_groups/
# Keeps detail GET unchanged.

from flask_restx import Namespace, Resource, fields
from ..models import DamGroup
from .. import db
from ..utils.pagination import get_pagination_params, envelope

dam_groups_bp = Namespace('DamGroups', description='Endpoints for managing dam groups')

group_model = dam_groups_bp.model('Group', {
    'group_name': fields.String(required=True, description='The name of the group'),
})

pagination_meta = dam_groups_bp.model('PaginationMeta', {
    'page': fields.Integer,
    'per_page': fields.Integer,
    'pages': fields.Integer,
    'total': fields.Integer,
})

pagination_links = dam_groups_bp.model('PaginationLinks', {
    'self': fields.String,
    'next': fields.String,
    'prev': fields.String,
})

group_list_envelope = dam_groups_bp.model('GroupListEnvelope', {
    'data': fields.List(fields.Nested(group_model)),
    'meta': fields.Nested(pagination_meta),
    'links': fields.Nested(pagination_links),
})


@dam_groups_bp.route('/', endpoint='dam_groups_list')
class GroupsList(Resource):
    @dam_groups_bp.doc('list_dam_groups')
    @dam_groups_bp.marshal_with(group_list_envelope)
    def get(self):
        """List all dam groups (paginated)"""
        page, per_page = get_pagination_params()
        return envelope(DamGroup.query, page, per_page, 'dam_groups_list')


@dam_groups_bp.route('/<string:group_name>', endpoint='dam_groups_detail')
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
