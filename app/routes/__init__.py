# app/routes/__init__.py

from flask import Blueprint

from .main import main_bp
from .dams import dams_bp
from .latest_data import latest_data_bp
from .dam_resources import dam_resources_bp
from .specific_dam_analysis import specific_dam_analysis_bp
from .overall_dam_analysis import overall_dam_analysis_bp
from .dam_groups import dam_groups_bp
from .dam_group_members import dam_group_members_bp
