# app/routes/specific_dam_analysis.py

from flask_restx import Namespace, Resource, fields
from ..models import SpecificDamAnalysis
from .. import db

specific_dam_analysis_bp = Namespace('SpecificDamAnalysis', description='Endpoints for specific dam analyses')

# Define a model for specific dam analysis
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


@specific_dam_analysis_bp.route('/')
class SpecificDamAnalysesList(Resource):
    @specific_dam_analysis_bp.doc('list_specific_dam_analyses')
    @specific_dam_analysis_bp.marshal_list_with(specific_dam_analysis_model)
    def get(self):
        """List all specific dam analyses"""
        analyses = SpecificDamAnalysis.query.all()
        return analyses


@specific_dam_analysis_bp.route('/<string:dam_id>')
@specific_dam_analysis_bp.param('dam_id', 'The ID of the dam')
class SpecificDamAnalysisDetail(Resource):
    @specific_dam_analysis_bp.doc('get_specific_dam_analysis')
    @specific_dam_analysis_bp.marshal_list_with(specific_dam_analysis_model)
    def get(self, dam_id):
        """Get specific dam analyses by dam ID"""
        analyses = SpecificDamAnalysis.query.filter_by(dam_id=dam_id).all()
        if not analyses:
            specific_dam_analysis_bp.abort(404, "Specific dam analyses not found for the specified dam.")
        return analyses
