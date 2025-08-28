# app/routes/dam_resources.py

from flask_restx import Namespace, Resource, fields
from ..models import DamResource
from ..utils.pagination import get_pagination_params, envelope
from ..utils.db import get_or_404

dam_resources_bp = Namespace('DamResources', description='Endpoints for managing dam resources')

resource_model = dam_resources_bp.model('Resource', {
    'resource_id': fields.Integer(required=True, description='The ID of the resource'),
    'dam_id': fields.String(required=True, description='The ID of the dam'),
    'date': fields.String(required=True, description='The date of the resource entry in ISO format'),
    'storage_volume': fields.Float(description='The storage volume'),
    'percentage_full': fields.Float(description='The percentage of the dam that is full'),
    'storage_inflow': fields.Float(description='The inflow to the dam'),
    'storage_release': fields.Float(description='The release from the dam'),
})

pagination_meta = dam_resources_bp.model('PaginationMeta', {
    'page': fields.Integer,
    'per_page': fields.Integer,
    'pages': fields.Integer,
    'total': fields.Integer,
})

pagination_links = dam_resources_bp.model('PaginationLinks', {
    'self': fields.String,
    'next': fields.String,
    'prev': fields.String,
})

resource_list_envelope = dam_resources_bp.model('ResourceListEnvelope', {
    'data': fields.List(fields.Nested(resource_model)),
    'meta': fields.Nested(pagination_meta),
    'links': fields.Nested(pagination_links),
})


@dam_resources_bp.route('/', endpoint='dam_resources_list')
class ResourcesList(Resource):
    @dam_resources_bp.doc('list_dam_resources')
    @dam_resources_bp.marshal_with(resource_list_envelope)
    def get(self):
        page, per_page = get_pagination_params()
        return envelope(DamResource.query, page, per_page, 'dam_resources_list')


@dam_resources_bp.route('/<int:resource_id>', endpoint='dam_resources_detail')
@dam_resources_bp.param('resource_id', 'The ID of the resource')
class Resource(Resource):
    @dam_resources_bp.doc('get_dam_resource')
    @dam_resources_bp.marshal_with(resource_model)
    def get(self, resource_id):
        return get_or_404(DamResource, resource_id, "Dam resource not found.")
