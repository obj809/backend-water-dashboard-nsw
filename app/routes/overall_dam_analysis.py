# app/routes/overall_dam_analysis.py

from datetime import date
from flask_restx import Namespace, Resource, fields
from ..models import OverallDamAnalysis
from .. import db

overall_dam_analysis_bp = Namespace('OverallDamAnalysis', description='Endpoints for overall dam analyses')

# Define a model for overall dam analysis
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


@overall_dam_analysis_bp.route('/')
class OverallDamAnalysesList(Resource):
    @overall_dam_analysis_bp.doc('list_overall_dam_analyses')
    @overall_dam_analysis_bp.marshal_list_with(overall_dam_analysis_model)
    def get(self):
        """List all overall dam analyses"""
        analyses = OverallDamAnalysis.query.all()
        return analyses


@overall_dam_analysis_bp.route('/<string:analysis_date>')
@overall_dam_analysis_bp.param('analysis_date', 'The date of the analysis in ISO format (YYYY-MM-DD)')
class OverallDamAnalysisDetail(Resource):
    @overall_dam_analysis_bp.doc('get_overall_dam_analysis')
    @overall_dam_analysis_bp.marshal_with(overall_dam_analysis_model)
    def get(self, analysis_date):
        """Get overall dam analysis by date"""
        try:
            analysis_date_obj = date.fromisoformat(analysis_date)
        except ValueError:
            overall_dam_analysis_bp.abort(400, "Invalid date format. Use YYYY-MM-DD.")
        
        analysis = OverallDamAnalysis.query.get(analysis_date_obj)
        if not analysis:
            overall_dam_analysis_bp.abort(404, "Overall dam analysis not found for the specified date.")
        return analysis
