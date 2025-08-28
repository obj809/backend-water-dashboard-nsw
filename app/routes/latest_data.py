# app/routes/latest_data.py

from flask_restx import Namespace, Resource, fields
from ..models import LatestData
from ..utils.pagination import get_pagination_params, envelope
from ..utils.db import get_or_404

latest_data_bp = Namespace('LatestData', description='Endpoints for managing latest dam data')

latest_data_model = latest_data_bp.model('LatestData', {
    'dam_id': fields.String(required=True, description='The ID of the dam'),
    'dam_name': fields.String(required=True, description='The name of the dam'),
    'date': fields.String(required=True, description='The date of the latest data entry in ISO format'),
    'storage_volume': fields.Float(description='The storage volume'),
    'percentage_full': fields.Float(description='The percentage of the dam that is full'),
    'storage_inflow': fields.Float(description='The inflow to the dam'),
    'storage_release': fields.Float(description='The release from the dam'),
})

pagination_meta = latest_data_bp.model('PaginationMeta', {
    'page': fields.Integer,
    'per_page': fields.Integer,
    'pages': fields.Integer,
    'total': fields.Integer,
})

pagination_links = latest_data_bp.model('PaginationLinks', {
    'self': fields.String,
    'next': fields.String,
    'prev': fields.String,
})

latest_data_list_envelope = latest_data_bp.model('LatestDataListEnvelope', {
    'data': fields.List(fields.Nested(latest_data_model)),
    'meta': fields.Nested(pagination_meta),
    'links': fields.Nested(pagination_links),
})


@latest_data_bp.route('/', endpoint='latest_data_list')
class LatestDataList(Resource):
    @latest_data_bp.doc('list_latest_data')
    @latest_data_bp.marshal_with(latest_data_list_envelope)
    def get(self):
        page, per_page = get_pagination_params()
        return envelope(LatestData.query, page, per_page, 'latest_data_list')


@latest_data_bp.route('/<string:dam_id>', endpoint='latest_data_detail')
@latest_data_bp.param('dam_id', 'The ID of the dam')
class LatestDataDetail(Resource):
    @latest_data_bp.doc('get_latest_data_by_dam')
    @latest_data_bp.marshal_with(latest_data_model)
    def get(self, dam_id):
        return get_or_404(LatestData, dam_id, "Latest data for the specified dam not found.")
