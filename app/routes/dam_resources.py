# app/routes/dam_resources.py

from flask_restx import Namespace, Resource, fields
from ..models import DamResource
from .. import db

dam_resources_bp = Namespace('DamResources', description='Endpoints for managing dam resources')

# Define a model for dam resources
resource_model = dam_resources_bp.model('Resource', {
    'resource_id': fields.Integer(required=True, description='The ID of the resource'),
    'dam_id': fields.String(required=True, description='The ID of the dam'),
    'date': fields.String(required=True, description='The date of the resource entry in ISO format'),
    'storage_volume': fields.Float(description='The storage volume'),
    'percentage_full': fields.Float(description='The percentage of the dam that is full'),
    'storage_inflow': fields.Float(description='The inflow to the dam'),
    'storage_release': fields.Float(description='The release from the dam'),
})


@dam_resources_bp.route('/')
class ResourcesList(Resource):
    @dam_resources_bp.doc('list_dam_resources')
    @dam_resources_bp.marshal_list_with(resource_model)
    def get(self):
        """List all dam resources"""
        resources = DamResource.query.all()
        return resources


@dam_resources_bp.route('/<int:resource_id>')
@dam_resources_bp.param('resource_id', 'The ID of the resource')
class Resource(Resource):
    @dam_resources_bp.doc('get_dam_resource')
    @dam_resources_bp.marshal_with(resource_model)
    def get(self, resource_id):
        """Get a dam resource by ID"""
        resource = DamResource.query.get(resource_id)
        if not resource:
            dam_resources_bp.abort(404, "Dam resource not found.")
        return resource
