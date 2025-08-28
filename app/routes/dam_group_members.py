# app/routes/dam_group_members.py
#
# Adds pagination to:
#   - GET /api/dam_group_members/
#   - GET /api/dam_group_members/<group_name>
#
# Uses utils.pagination.get_pagination_params + envelope()
# and defines a Swagger "envelope" for consistent response shapes.

from flask_restx import Namespace, Resource, fields
from ..models import DamGroupMember
from .. import db
from ..utils.pagination import get_pagination_params, envelope

dam_group_members_bp = Namespace('DamGroupMembers', description='Endpoints for managing dam group members')

# Item model
group_member_model = dam_group_members_bp.model('GroupMember', {
    'group_name': fields.String(required=True, description='The name of the group'),
    'dam_id': fields.String(required=True, description='The ID of the dam'),
})

# Meta/Links models for pagination
pagination_meta = dam_group_members_bp.model('PaginationMeta', {
    'page': fields.Integer,
    'per_page': fields.Integer,
    'pages': fields.Integer,
    'total': fields.Integer,
})

pagination_links = dam_group_members_bp.model('PaginationLinks', {
    'self': fields.String,
    'next': fields.String,
    'prev': fields.String,
})

# Envelope model for paginated list
group_member_list_envelope = dam_group_members_bp.model('GroupMemberListEnvelope', {
    'data': fields.List(fields.Nested(group_member_model)),
    'meta': fields.Nested(pagination_meta),
    'links': fields.Nested(pagination_links),
})


@dam_group_members_bp.route('/', endpoint='dam_group_members_list')
class GroupMembersList(Resource):
    @dam_group_members_bp.doc('list_dam_group_members')
    @dam_group_members_bp.marshal_with(group_member_list_envelope)
    def get(self):
        """List all dam group members (paginated)"""
        page, per_page = get_pagination_params()
        return envelope(DamGroupMember.query, page, per_page, 'dam_group_members_list')


@dam_group_members_bp.route('/<string:group_name>', endpoint='dam_group_members_by_group')
@dam_group_members_bp.param('group_name', 'The name of the group')
class GroupMembersByGroup(Resource):
    @dam_group_members_bp.doc('get_members_by_group')
    @dam_group_members_bp.marshal_with(group_member_list_envelope)
    def get(self, group_name):
        """Get members by group name (paginated)"""
        page, per_page = get_pagination_params()
        q = DamGroupMember.query.filter_by(group_name=group_name)
        items = q.paginate(page=page, per_page=per_page, error_out=False)
        if items.total == 0:
            dam_group_members_bp.abort(404, "No members found for the specified group.")
        return envelope(q, page, per_page, 'dam_group_members_by_group', group_name=group_name)
