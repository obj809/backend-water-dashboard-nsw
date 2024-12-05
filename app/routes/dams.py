# app/routes/dams.py

from flask_restx import Namespace, Resource, fields
from ..models import Dam
from .. import db

dams_bp = Namespace('Dams', description='Endpoints for managing dams')

# Define a model for dams
dam_model = dams_bp.model('Dam', {
    'dam_id': fields.String(required=True, description='The ID of the dam'),
    'dam_name': fields.String(required=True, description='The name of the dam'),
    'full_volume': fields.Integer(description='The full volume of the dam'),
    'latitude': fields.Float(description='The latitude of the dam'),
    'longitude': fields.Float(description='The longitude of the dam'),
})


@dams_bp.route('/')
class DamsList(Resource):
    @dams_bp.doc('list_dams')
    @dams_bp.marshal_list_with(dam_model)
    def get(self):
        """List all dams"""
        dams = Dam.query.all()
        return dams


@dams_bp.route('/<string:dam_id>')
@dams_bp.param('dam_id', 'The ID of the dam')
class DamDetail(Resource):
    @dams_bp.doc('get_dam')
    @dams_bp.marshal_with(dam_model)
    def get(self, dam_id):
        """Get a dam by ID"""
        dam = Dam.query.get(dam_id)
        if not dam:
            dams_bp.abort(404, "Dam not found.")
        return dam
