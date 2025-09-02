# app/routes/latest_data.py

from flask_restx import Namespace, Resource, fields
from ..models import LatestData
from ..utils.db import get_or_404

latest_data_bp = Namespace('LatestData', description='Endpoints for managing latest dam data')

class ISODate(fields.Raw):
    def format(self, value):
        return value.isoformat() if value else None

latest_data_model = latest_data_bp.model('LatestData', {
    'dam_id': fields.String(required=True, description='The ID of the dam'),
    'dam_name': fields.String(required=True, description='The name of the dam'),
    'date': ISODate(required=True, description='ISO date'),
    'storage_volume': fields.Float(description='The storage volume', allow_null=True),
    'percentage_full': fields.Float(description='The percentage of the dam that is full', allow_null=True),
    'storage_inflow': fields.Float(description='The inflow to the dam', allow_null=True),
    'storage_release': fields.Float(description='The release from the dam', allow_null=True),
})

@latest_data_bp.route('/', endpoint='latest_data_list')
class LatestDataList(Resource):
    @latest_data_bp.doc('list_latest_data')
    @latest_data_bp.marshal_list_with(latest_data_model)
    def get(self):
        return LatestData.query.all()

@latest_data_bp.route('/<string:dam_id>', endpoint='latest_data_detail')
@latest_data_bp.param('dam_id', 'The ID of the dam')
class LatestDataDetail(Resource):
    @latest_data_bp.doc('get_latest_data_by_dam')
    @latest_data_bp.marshal_with(latest_data_model)
    def get(self, dam_id):
        return get_or_404(LatestData, dam_id, "Latest data for the specified dam not found.")
