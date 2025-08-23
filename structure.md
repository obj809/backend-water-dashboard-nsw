backend-sydney-dam-monitoring/
├─ run.py
├─ requirements.txt
├─ db_schema/
│  └─ db_schema.sql
├─ app/
│  ├─ __init__.py            # create_app(): Flask, SQLAlchemy, Migrate, CORS, RESTx Api
│  ├─ config.py              # Config + validate() -> requires SQLALCHEMY_DATABASE_URI
│  ├─ models.py              # SQLAlchemy models (Dams, Data, Analyses, Groups, Members)
│  └─ routes/
│     ├─ __init__.py         # imports and exposes Namespaces
│     ├─ main.py             # GET /api/ → welcome
│     ├─ dams.py             # /api/dams
│     ├─ latest_data.py      # /api/latest_data
│     ├─ dam_resources.py    # /api/dam_resources
│     ├─ specific_dam_analysis.py   # /api/specific_dam_analysis
│     ├─ overall_dam_analysis.py    # /api/overall_dam_analysis
│     ├─ dam_groups.py       # /api/dam_groups
│     └─ dam_group_members.py# /api/dam_group_members
└─ scripts/
   ├─ db_connection_check.py
   ├─ collect_data.py
   ├─ export_table_records.py
   ├─ insert_dam_analysis_data.py
   ├─ data_collection_and_export.py
   └─ test_api_endpoints.py
