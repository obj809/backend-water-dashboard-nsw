# app/routes/specific_dam_analysis.py

from flask import Blueprint, jsonify, abort
from ..models import SpecificDamAnalysis
from .. import db

specific_dam_analysis_bp = Blueprint('specific_dam_analysis_bp', __name__, url_prefix='/api/specific_dam_analysis')

@specific_dam_analysis_bp.route('/', methods=['GET'])
def get_specific_dam_analyses():
    analyses = SpecificDamAnalysis.query.all()
    return jsonify([{
        'dam_id': analysis.dam_id,
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

@specific_dam_analysis_bp.route('/<string:dam_id>', methods=['GET'])
def get_specific_dam_analysis(dam_id):
    analyses = SpecificDamAnalysis.query.filter_by(dam_id=dam_id).all()
    if not analyses:
        abort(404, description="Specific dam analyses not found for the specified dam.")
    return jsonify([{
        'dam_id': analysis.dam_id,
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
