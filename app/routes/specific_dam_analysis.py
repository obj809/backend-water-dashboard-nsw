# app/routes/specific_dam_analysis.py


from flask_restx import Namespace, Resource, fields
from ..models import SpecificDamAnalysis
from ..utils.pagination import get_pagination_params, envelope
from ..utils.db import get_or_404
from ..utils.dates import parse_iso_date

specific_dam_analysis_bp = Namespace('SpecificDamAnalysis', description='Endpoints for specific dam analyses')

specific_dam_analysis_model = specific_dam_analysis_bp.model('SpecificDamAnalysis', {
    'dam_id': fields.String(required=True, description='The ID of the dam'),
    'analysis_date': fields.String(required=True, description='The date of the analysis in ISO format'),
    'avg_storage_volume_12_months': fields.Float(description='Average storage volume over 12 months'),
    'avg_storage_volume_5_years': fields.Float(description='Average storage volume over 5 years'),
    'avg_storage_volume_20_years': fields.Float(description='Average storage volume over 20 years'),
    'avg_percentage_full_12_months': fields.Float(description='Average percentage full over 12 months'),
    'avg_percentage_full_5_years': fields.Float(description='Average percentage full over 5 years'),
    'avg_percentage_full_20_years': fields.Float(description='Average percentage full over 20 years'),
    'avg_storage_inflow_12_months': fields.Float(description='Average inflow over 12 months'),
    'avg_storage_inflow_5_years': fields.Float(description='Average inflow over 5 years'),
    'avg_storage_inflow_20_years': fields.Float(description='Average inflow over 20 years'),
    'avg_storage_release_12_months': fields.Float(description='Average release over 12 months'),
    'avg_storage_release_5_years': fields.Float(description='Average release over 5 years'),
    'avg_storage_release_20_years': fields.Float(description='Average release over 20 years'),
})

pagination_meta = specific_dam_analysis_bp.model('PaginationMeta', {
    'page': fields.Integer,
    'per_page': fields.Integer,
    'pages': fields.Integer,
    'total': fields.Integer,
})

pagination_links = specific_dam_analysis_bp.model('PaginationLinks', {
    'self': fields.String,
    'next': fields.String,
    'prev': fields.String,
})

specific_list_envelope = specific_dam_analysis_bp.model('SpecificDamAnalysisListEnvelope', {
    'data': fields.List(fields.Nested(specific_dam_analysis_model)),
    'meta': fields.Nested(pagination_meta),
    'links': fields.Nested(pagination_links),
})


@specific_dam_analysis_bp.route('/', endpoint='specific_dam_analysis_list')
class SpecificDamAnalysesList(Resource):
    @specific_dam_analysis_bp.doc('list_specific_dam_analyses')
    @specific_dam_analysis_bp.marshal_with(specific_list_envelope)
    def get(self):
        page, per_page = get_pagination_params()
        return envelope(SpecificDamAnalysis.query, page, per_page, 'specific_dam_analysis_list')


@specific_dam_analysis_bp.route('/<string:dam_id>', endpoint='specific_dam_analysis_by_dam')
@specific_dam_analysis_bp.param('dam_id', 'The ID of the dam')
class SpecificDamAnalysisDetail(Resource):
    @specific_dam_analysis_bp.doc('get_specific_dam_analysis')
    @specific_dam_analysis_bp.marshal_with(specific_list_envelope)
    def get(self, dam_id):
        page, per_page = get_pagination_params()
        q = SpecificDamAnalysis.query.filter_by(dam_id=dam_id)
        items = q.paginate(page=page, per_page=per_page, error_out=False)
        if items.total == 0:
            specific_dam_analysis_bp.abort(404, "Specific dam analyses not found for the specified dam.")
        return envelope(q, page, per_page, 'specific_dam_analysis_by_dam', dam_id=dam_id)


@specific_dam_analysis_bp.route('/<string:dam_id>/<string:analysis_date>', endpoint='specific_dam_analysis_detail')
@specific_dam_analysis_bp.param('dam_id', 'The ID of the dam')
@specific_dam_analysis_bp.param('analysis_date', 'The date of the analysis in ISO format (YYYY-MM-DD)')
class SpecificDamAnalysisDetailByPK(Resource):
    @specific_dam_analysis_bp.doc('get_specific_dam_analysis_detail')
    @specific_dam_analysis_bp.marshal_with(specific_dam_analysis_model)
    def get(self, dam_id, analysis_date):
        analysis_date_obj = parse_iso_date(analysis_date)
        return get_or_404(
            SpecificDamAnalysis,
            (dam_id, analysis_date_obj),
            "Specific dam analysis not found for the specified dam/date."
        )
