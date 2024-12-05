# app/routes/overall_dam_analysis.py

from datetime import date  # Ensure this import is present
from flask import Blueprint, jsonify, abort
from ..models import OverallDamAnalysis
from .. import db

overall_dam_analysis_bp = Blueprint('overall_dam_analysis_bp', __name__, url_prefix='/api/overall_dam_analysis')

@overall_dam_analysis_bp.route('/', methods=['GET'])
def get_overall_dam_analyses():
    analyses = OverallDamAnalysis.query.all()
    return jsonify([{
        'analysis_date': analysis.analysis_date.isoformat(),
        'avg_storage_volume_12_months': float(analysis.avg_storage_volume_12_months) if analysis.avg_storage_volume_12_months else None,
        'avg_storage_volume_5_years': float(analysis.avg_storage_volume_5_years) if analysis.avg_storage_volume_5_years else None,
        'avg_storage_volume_20_years': float(analysis.avg_storage_volume_20_years) if analysis.avg_storage_volume_20_years else None,
        'avg_percentage_full_12_months': float(analysis.avg_percentage_full_12_months) if analysis.avg_percentage_full_12_months else None,
        'avg_percentage_full_5_years': float(analysis.avg_percentage_full_5_years) if analysis.avg_percentage_full_5_years else None,
        'avg_percentage_full_20_years': float(analysis.avg_percentage_full_20_years) if analysis.avg_percentage_full_20_years else None,
        'avg_storage_inflow_12_months': float(analysis.avg_storage_inflow_12_months) if analysis.avg_storage_inflow_12_months else None,
        'avg_storage_inflow_5_years': float(analysis.avg_storage_inflow_5_years) if analysis.avg_storage_inflow_5_years else None,
        'avg_storage_inflow_20_years': float(analysis.avg_storage_inflow_20_years) if analysis.avg_storage_inflow_20_years else None,
        'avg_storage_release_12_months': float(analysis.avg_storage_release_12_months) if analysis.avg_storage_release_12_months else None,
        'avg_storage_release_5_years': float(analysis.avg_storage_release_5_years) if analysis.avg_storage_release_5_years else None,
        'avg_storage_release_20_years': float(analysis.avg_storage_release_20_years) if analysis.avg_storage_release_20_years else None
    } for analysis in analyses])

@overall_dam_analysis_bp.route('/<string:analysis_date>', methods=['GET'])
def get_overall_dam_analysis(analysis_date):
    try:
        analysis_date_obj = date.fromisoformat(analysis_date)
    except ValueError:
        abort(400, description="Invalid date format. Use YYYY-MM-DD.")
    
    analysis = OverallDamAnalysis.query.get(analysis_date_obj)
    if not analysis:
        abort(404, description="Overall dam analysis not found for the specified date.")
    return jsonify({
        'analysis_date': analysis.analysis_date.isoformat(),
        'avg_storage_volume_12_months': float(analysis.avg_storage_volume_12_months) if analysis.avg_storage_volume_12_months else None,
        'avg_storage_volume_5_years': float(analysis.avg_storage_volume_5_years) if analysis.avg_storage_volume_5_years else None,
        'avg_storage_volume_20_years': float(analysis.avg_storage_volume_20_years) if analysis.avg_storage_volume_20_years else None,
        'avg_percentage_full_12_months': float(analysis.avg_percentage_full_12_months) if analysis.avg_percentage_full_12_months else None,
        'avg_percentage_full_5_years': float(analysis.avg_percentage_full_5_years) if analysis.avg_percentage_full_5_years else None,
        'avg_percentage_full_20_years': float(analysis.avg_percentage_full_20_years) if analysis.avg_percentage_full_20_years else None,
        'avg_storage_inflow_12_months': float(analysis.avg_storage_inflow_12_months) if analysis.avg_storage_inflow_12_months else None,
        'avg_storage_inflow_5_years': float(analysis.avg_storage_inflow_5_years) if analysis.avg_storage_inflow_5_years else None,
        'avg_storage_inflow_20_years': float(analysis.avg_storage_inflow_20_years) if analysis.avg_storage_inflow_20_years else None,
        'avg_storage_release_12_months': float(analysis.avg_storage_release_12_months) if analysis.avg_storage_release_12_months else None,
        'avg_storage_release_5_years': float(analysis.avg_storage_release_5_years) if analysis.avg_storage_release_5_years else None,
        'avg_storage_release_20_years': float(analysis.avg_storage_release_20_years) if analysis.avg_storage_release_20_years else None
    })
