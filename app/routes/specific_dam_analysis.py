# app/routes/specific_dam_analysis.py

from flask_restx import Namespace, Resource, fields
from ..models import SpecificDamAnalysis
from ..utils.db import get_or_404
from ..utils.dates import parse_iso_date

specific_dam_analysis_bp = Namespace('SpecificDamAnalysis', description='Endpoints for specific dam analyses')

class ISODate(fields.Raw):
    def format(self, value):
        return value.isoformat() if value else None

specific_dam_analysis_model = specific_dam_analysis_bp.model('SpecificDamAnalysis', {
    'dam_id': fields.String(required=True, description='The ID of the dam'),
    'analysis_date': ISODate(required=True, description='ISO date'),
    'avg_storage_volume_12_months': fields.Float(allow_null=True),
    'avg_storage_volume_5_years': fields.Float(allow_null=True),
    'avg_storage_volume_10_years': fields.Float(allow_null=True),
    'avg_percentage_full_12_months': fields.Float(allow_null=True),
    'avg_percentage_full_5_years': fields.Float(allow_null=True),
    'avg_percentage_full_10_years': fields.Float(allow_null=True),
    'avg_storage_inflow_12_months': fields.Float(allow_null=True),
    'avg_storage_inflow_5_years': fields.Float(allow_null=True),
    'avg_storage_inflow_10_years': fields.Float(allow_null=True),
    'avg_storage_release_12_months': fields.Float(allow_null=True),
    'avg_storage_release_5_years': fields.Float(allow_null=True),
    'avg_storage_release_10_years': fields.Float(allow_null=True),
})

@specific_dam_analysis_bp.route('/', endpoint='specific_dam_analysis_list')
class SpecificDamAnalysesList(Resource):
    @specific_dam_analysis_bp.doc('list_specific_dam_analyses')
    @specific_dam_analysis_bp.marshal_list_with(specific_dam_analysis_model)
    def get(self):
        return SpecificDamAnalysis.query.all()

@specific_dam_analysis_bp.route('/<string:dam_id>', endpoint='specific_dam_analysis_by_dam')
@specific_dam_analysis_bp.param('dam_id', 'The ID of the dam')
class SpecificDamAnalysisByDam(Resource):
    @specific_dam_analysis_bp.doc('get_specific_dam_analysis_by_dam')
    @specific_dam_analysis_bp.marshal_list_with(specific_dam_analysis_model)
    def get(self, dam_id):
        items = SpecificDamAnalysis.query.filter_by(dam_id=dam_id).all()
        if not items:
            specific_dam_analysis_bp.abort(404, "Specific dam analyses not found for the specified dam.")
        return items

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
