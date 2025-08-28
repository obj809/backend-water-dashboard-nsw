# app/routes/dams.py
#
# Modernizes PK lookups using db.session.get via get_or_404 helper.
# Keeps pagination for list endpoint.

from flask_restx import Namespace, Resource, fields
from ..models import Dam
from ..utils.pagination import get_pagination_params, envelope
from ..utils.db import get_or_404

dams_bp = Namespace('Dams', description='Endpoints for managing dams')

dam_model = dams_bp.model('Dam', {
    'dam_id': fields.String(required=True, description='The ID of the dam'),
    'dam_name': fields.String(required=True, description='The name of the dam'),
    'full_volume': fields.Integer(description='The full volume of the dam'),
    'latitude': fields.Float(description='The latitude of the dam'),
    'longitude': fields.Float(description='The longitude of the dam'),
})

pagination_meta = dams_bp.model('PaginationMeta', {
    'page': fields.Integer,
    'per_page': fields.Integer,
    'pages': fields.Integer,
    'total': fields.Integer,
})

pagination_links = dams_bp.model('PaginationLinks', {
    'self': fields.String,
    'next': fields.String,
    'prev': fields.String,
})

dam_list_envelope = dams_bp.model('DamListEnvelope', {
    'data': fields.List(fields.Nested(dam_model)),
    'meta': fields.Nested(pagination_meta),
    'links': fields.Nested(pagination_links),
})


@dams_bp.route('/', endpoint='dams_list')
class DamsList(Resource):
    @dams_bp.doc('list_dams')
    @dams_bp.marshal_with(dam_list_envelope)
    def get(self):
        """List all dams (paginated)"""
        page, per_page = get_pagination_params()
        from ..models import Dam  # local import not necessary, but explicit for clarity
        return envelope(Dam.query, page, per_page, 'dams_list')


@dams_bp.route('/<string:dam_id>', endpoint='dams_detail')
@dams_bp.param('dam_id', 'The ID of the dam')
class DamDetail(Resource):
    @dams_bp.doc('get_dam')
    @dams_bp.marshal_with(dam_model)
    def get(self, dam_id):
        """Get a dam by ID"""
        dam = get_or_404(Dam, dam_id, "Dam not found.")
        return dam
