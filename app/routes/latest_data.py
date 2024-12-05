# app/routes/latest_data.py

from flask_restx import Namespace, Resource, fields
from ..models import LatestData
from .. import db

latest_data_bp = Namespace('LatestData', description='Endpoints for managing latest dam data')

# Define a model for latest dam data
latest_data_model = latest_data_bp.model('LatestData', {
    'dam_id': fields.String(required=True, description='The ID of the dam'),
    'dam_name': fields.String(required=True, description='The name of the dam'),
    'date': fields.String(required=True, description='The date of the latest data entry in ISO format'),
    'storage_volume': fields.Float(description='The storage volume'),
    'percentage_full': fields.Float(description='The percentage of the dam that is full'),
    'storage_inflow': fields.Float(description='The inflow to the dam'),
    'storage_release': fields.Float(description='The release from the dam'),
})


@latest_data_bp.route('/')
class LatestDataList(Resource):
    @latest_data_bp.doc('list_latest_data')
    @latest_data_bp.marshal_list_with(latest_data_model)
    def get(self):
        """List all latest dam data entries"""
        data_entries = LatestData.query.all()
        return data_entries


@latest_data_bp.route('/<string:dam_id>')
@latest_data_bp.param('dam_id', 'The ID of the dam')
class LatestDataDetail(Resource):
    @latest_data_bp.doc('get_latest_data_by_dam')
    @latest_data_bp.marshal_with(latest_data_model)
    def get(self, dam_id):
        """Get the latest data for a specific dam by ID"""
        data = LatestData.query.get(dam_id)
        if not data:
            latest_data_bp.abort(404, "Latest data for the specified dam not found.")
        return data
