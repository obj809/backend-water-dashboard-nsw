# app/routes/overall_dam_analysis.py


from flask_restx import Namespace, Resource, fields
from ..models import OverallDamAnalysis
from ..utils.pagination import get_pagination_params, envelope
from ..utils.db import get_or_404
from ..utils.dates import parse_iso_date

overall_dam_analysis_bp = Namespace('OverallDamAnalysis', description='Endpoints for overall dam analyses')

overall_dam_analysis_model = overall_dam_analysis_bp.model('OverallDamAnalysis', {
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

pagination_meta = overall_dam_analysis_bp.model('PaginationMeta', {
    'page': fields.Integer,
    'per_page': fields.Integer,
    'pages': fields.Integer,
    'total': fields.Integer,
})

pagination_links = overall_dam_analysis_bp.model('PaginationLinks', {
    'self': fields.String,
    'next': fields.String,
    'prev': fields.String,
})

overall_list_envelope = overall_dam_analysis_bp.model('OverallDamAnalysisListEnvelope', {
    'data': fields.List(fields.Nested(overall_dam_analysis_model)),
    'meta': fields.Nested(pagination_meta),
    'links': fields.Nested(pagination_links),
})


@overall_dam_analysis_bp.route('/', endpoint='overall_dam_analysis_list')
class OverallDamAnalysesList(Resource):
    @overall_dam_analysis_bp.doc('list_overall_dam_analyses')
    @overall_dam_analysis_bp.marshal_with(overall_list_envelope)
    def get(self):
        page, per_page = get_pagination_params()
        return envelope(OverallDamAnalysis.query, page, per_page, 'overall_dam_analysis_list')


@overall_dam_analysis_bp.route('/<string:analysis_date>', endpoint='overall_dam_analysis_detail')
@overall_dam_analysis_bp.param('analysis_date', 'The date of the analysis in ISO format (YYYY-MM-DD)')
class OverallDamAnalysisDetail(Resource):
    @overall_dam_analysis_bp.doc('get_overall_dam_analysis')
    @overall_dam_analysis_bp.marshal_with(overall_dam_analysis_model)
    def get(self, analysis_date):
        analysis_date_obj = parse_iso_date(analysis_date)
        return get_or_404(OverallDamAnalysis, analysis_date_obj,
                          "Overall dam analysis not found for the specified date.")
