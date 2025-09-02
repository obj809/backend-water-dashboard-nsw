# app/routes/overall_dam_analysis.py


from flask_restx import Namespace, Resource, fields
from ..models import OverallDamAnalysis
from ..utils.db import get_or_404
from ..utils.dates import parse_iso_date

overall_dam_analysis_bp = Namespace('OverallDamAnalysis', description='Endpoints for overall dam analyses')

class ISODate(fields.Raw):
    def format(self, value):
        return value.isoformat() if value else None

overall_dam_analysis_model = overall_dam_analysis_bp.model('OverallDamAnalysis', {
    'analysis_date': ISODate(required=True, description='ISO date'),
    'avg_storage_volume_12_months': fields.Float(allow_null=True),
    'avg_storage_volume_5_years': fields.Float(allow_null=True),
    'avg_storage_volume_20_years': fields.Float(allow_null=True),
    'avg_percentage_full_12_months': fields.Float(allow_null=True),
    'avg_percentage_full_5_years': fields.Float(allow_null=True),
    'avg_percentage_full_20_years': fields.Float(allow_null=True),
    'avg_storage_inflow_12_months': fields.Float(allow_null=True),
    'avg_storage_inflow_5_years': fields.Float(allow_null=True),
    'avg_storage_inflow_20_years': fields.Float(allow_null=True),
    'avg_storage_release_12_months': fields.Float(allow_null=True),
    'avg_storage_release_5_years': fields.Float(allow_null=True),
    'avg_storage_release_20_years': fields.Float(allow_null=True),
})

@overall_dam_analysis_bp.route('/', endpoint='overall_dam_analysis_list')
class OverallDamAnalysesList(Resource):
    @overall_dam_analysis_bp.doc('list_overall_dam_analyses')
    @overall_dam_analysis_bp.marshal_list_with(overall_dam_analysis_model)
    def get(self):
        return OverallDamAnalysis.query.all()

@overall_dam_analysis_bp.route('/<string:analysis_date>', endpoint='overall_dam_analysis_detail')
@overall_dam_analysis_bp.param('analysis_date', 'The date of the analysis in ISO format (YYYY-MM-DD)')
class OverallDamAnalysisDetail(Resource):
    @overall_dam_analysis_bp.doc('get_overall_dam_analysis')
    @overall_dam_analysis_bp.marshal_with(overall_dam_analysis_model)
    def get(self, analysis_date):
        analysis_date_obj = parse_iso_date(analysis_date)
        return get_or_404(OverallDamAnalysis, analysis_date_obj,
                          "Overall dam analysis not found for the specified date.")
