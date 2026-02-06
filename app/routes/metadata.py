# app/routes/metadata.py

from flask_restx import Namespace, Resource, fields
from sqlalchemy import func
from ..models import LatestData

metadata_bp = Namespace('Metadata', description='Application metadata endpoints')

class ISODate(fields.Raw):
    def format(self, value):
        return value.isoformat() if value else None

metadata_model = metadata_bp.model('Metadata', {
    'latest_data_date': ISODate(required=True, description='The date of the most recent data in the latest_data table'),
})

@metadata_bp.route('/', endpoint='metadata')
class Metadata(Resource):
    @metadata_bp.doc('get_metadata')
    @metadata_bp.marshal_with(metadata_model)
    def get(self):
        """Get application metadata including the latest data date"""
        # Query for the most recent date in the latest_data table
        latest_date = LatestData.query.with_entities(
            func.max(LatestData.date)
        ).scalar()

        return {
            'latest_data_date': latest_date
        }
