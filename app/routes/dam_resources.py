# app/routes/dam_resources.py

from flask_restx import Namespace, Resource, fields
from ..models import DamResource
from ..utils.db import get_or_404

dam_resources_bp = Namespace('DamResources', description='Endpoints for managing dam resources')

class ISODate(fields.Raw):
    def format(self, value):
        return value.isoformat() if value else None

resource_model = dam_resources_bp.model('Resource', {
    'resource_id': fields.Integer(required=True, description='The ID of the resource'),
    'dam_id': fields.String(required=True, description='The ID of the dam'),
    'date': ISODate(required=True, description='ISO date'),
    'storage_volume': fields.Float(description='The storage volume', allow_null=True),
    'percentage_full': fields.Float(description='The percentage of the dam that is full', allow_null=True),
    'storage_inflow': fields.Float(description='The inflow to the dam', allow_null=True),
    'storage_release': fields.Float(description='The release from the dam', allow_null=True),
})

@dam_resources_bp.route('/', endpoint='dam_resources_list')
class ResourcesList(Resource):
    @dam_resources_bp.doc('list_dam_resources')
    @dam_resources_bp.marshal_list_with(resource_model)
    def get(self):
        return DamResource.query.all()

@dam_resources_bp.route('/<int:resource_id>', endpoint='dam_resources_detail')
@dam_resources_bp.param('resource_id', 'The ID of the resource')
class Resource(Resource):
    @dam_resources_bp.doc('get_dam_resource')
    @dam_resources_bp.marshal_with(resource_model)
    def get(self, resource_id):
        return get_or_404(DamResource, resource_id, "Dam resource not found.")
