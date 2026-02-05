# app/models.py

from . import db
from datetime import date

class Dam(db.Model):
    __tablename__ = 'dams'
    dam_id = db.Column(db.String(20), primary_key=True)
    dam_name = db.Column(db.String(255), nullable=False)
    full_volume = db.Column(db.Integer)
    latitude = db.Column(db.Numeric(10, 6))
    longitude = db.Column(db.Numeric(10, 6))
    
    latest_data = db.relationship('LatestData', backref='dam', uselist=False)
    dam_resources = db.relationship('DamResource', backref='dam', lazy=True)
    specific_dam_analyses = db.relationship('SpecificDamAnalysis', backref='dam', lazy=True)
    dam_group_members = db.relationship('DamGroupMember', backref='dam', lazy=True)


class LatestData(db.Model):
    __tablename__ = 'latest_data'
    dam_id = db.Column(db.String(20), db.ForeignKey('dams.dam_id'), primary_key=True)
    dam_name = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, nullable=False)
    storage_volume = db.Column(db.Numeric(10, 3))
    percentage_full = db.Column(db.Numeric(6, 2))
    storage_inflow = db.Column(db.Numeric(10, 3))
    storage_release = db.Column(db.Numeric(10, 3))


class DamResource(db.Model):
    __tablename__ = 'dam_resources'
    resource_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dam_id = db.Column(db.String(20), db.ForeignKey('dams.dam_id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    storage_volume = db.Column(db.Numeric(10, 3))
    percentage_full = db.Column(db.Numeric(6, 2))
    storage_inflow = db.Column(db.Numeric(10, 3))
    storage_release = db.Column(db.Numeric(10, 3))


class SpecificDamAnalysis(db.Model):
    __tablename__ = 'specific_dam_analysis'
    dam_id = db.Column(db.String(20), db.ForeignKey('dams.dam_id'), primary_key=True)
    analysis_date = db.Column(db.Date, primary_key=True)
    avg_storage_volume_12_months = db.Column(db.Numeric(10, 3))
    avg_storage_volume_5_years = db.Column(db.Numeric(10, 3))
    avg_storage_volume_10_years = db.Column(db.Numeric(10, 3))
    avg_percentage_full_12_months = db.Column(db.Numeric(6, 2))
    avg_percentage_full_5_years = db.Column(db.Numeric(6, 2))
    avg_percentage_full_10_years = db.Column(db.Numeric(6, 2))
    avg_storage_inflow_12_months = db.Column(db.Numeric(10, 3))
    avg_storage_inflow_5_years = db.Column(db.Numeric(10, 3))
    avg_storage_inflow_10_years = db.Column(db.Numeric(10, 3))
    avg_storage_release_12_months = db.Column(db.Numeric(10, 3))
    avg_storage_release_5_years = db.Column(db.Numeric(10, 3))
    avg_storage_release_10_years = db.Column(db.Numeric(10, 3))


class OverallDamAnalysis(db.Model):
    __tablename__ = 'overall_dam_analysis'
    analysis_date = db.Column(db.Date, primary_key=True)
    avg_storage_volume_12_months = db.Column(db.Numeric(10, 3))
    avg_storage_volume_5_years = db.Column(db.Numeric(10, 3))
    avg_storage_volume_10_years = db.Column(db.Numeric(10, 3))
    avg_percentage_full_12_months = db.Column(db.Numeric(6, 2))
    avg_percentage_full_5_years = db.Column(db.Numeric(6, 2))
    avg_percentage_full_10_years = db.Column(db.Numeric(6, 2))
    avg_storage_inflow_12_months = db.Column(db.Numeric(10, 3))
    avg_storage_inflow_5_years = db.Column(db.Numeric(10, 3))
    avg_storage_inflow_10_years = db.Column(db.Numeric(10, 3))
    avg_storage_release_12_months = db.Column(db.Numeric(10, 3))
    avg_storage_release_5_years = db.Column(db.Numeric(10, 3))
    avg_storage_release_10_years = db.Column(db.Numeric(10, 3))


class DamGroup(db.Model):
    __tablename__ = 'dam_groups'
    group_name = db.Column(db.String(255), primary_key=True)
    members = db.relationship('DamGroupMember', backref='group', lazy=True)


class DamGroupMember(db.Model):
    __tablename__ = 'dam_group_members'
    group_name = db.Column(db.String(255), db.ForeignKey('dam_groups.group_name'), primary_key=True)
    dam_id = db.Column(db.String(20), db.ForeignKey('dams.dam_id'), primary_key=True)
