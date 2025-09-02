# scripts/insert_specific_dam_analysis_data.py

# import os
# import logging
# from datetime import date
# from typing import Optional, Mapping, Any

# from sqlalchemy import create_engine, text
# from dotenv import load_dotenv

# load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

# database_uri = os.getenv("SQLALCHEMY_DATABASE_URI")

# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
# logger = logging.getLogger()

# def insert_specific_dam_analysis_data(analysis_date: Optional[date] = None):

#     try:
#         if analysis_date is None:
#             analysis_date = date.today()

#         engine = create_engine(database_uri)

#         def avg_window_sql(months: int):
#             return text(f"""
#                 SELECT
#                     AVG(storage_volume)  AS avg_storage_volume,
#                     AVG(percentage_full) AS avg_percentage_full,
#                     AVG(storage_inflow)  AS avg_storage_inflow,
#                     AVG(storage_release) AS avg_storage_release
#                 FROM dam_resources
#                 WHERE dam_id = :dam_id
#                   AND `date` >= DATE_SUB(CURDATE(), INTERVAL {int(months)} MONTH)
#             """)

#         latest_sql = text("""
#             SELECT
#                 storage_volume  AS latest_storage_volume,
#                 percentage_full AS latest_percentage_full,
#                 storage_inflow  AS latest_storage_inflow,
#                 storage_release AS latest_storage_release
#             FROM latest_data
#             WHERE dam_id = :dam_id
#             LIMIT 1
#         """)

#         upsert_sql = text("""
#             INSERT INTO specific_dam_analysis (
#                 dam_id,
#                 analysis_date,
#                 avg_storage_volume_12_months,
#                 avg_storage_volume_5_years,
#                 avg_storage_volume_20_years,
#                 avg_percentage_full_12_months,
#                 avg_percentage_full_5_years,
#                 avg_percentage_full_20_years,
#                 avg_storage_inflow_12_months,
#                 avg_storage_inflow_5_years,
#                 avg_storage_inflow_20_years,
#                 avg_storage_release_12_months,
#                 avg_storage_release_5_years,
#                 avg_storage_release_20_years
#             )
#             VALUES (
#                 :dam_id,
#                 :analysis_date,
#                 :avg_vol_12,
#                 :avg_vol_60,
#                 :avg_vol_240,
#                 :avg_pct_12,
#                 :avg_pct_60,
#                 :avg_pct_240,
#                 :avg_in_12,
#                 :avg_in_60,
#                 :avg_in_240,
#                 :avg_out_12,
#                 :avg_out_60,
#                 :avg_out_240
#             )
#             ON DUPLICATE KEY UPDATE
#                 avg_storage_volume_12_months  = VALUES(avg_storage_volume_12_months),
#                 avg_storage_volume_5_years    = VALUES(avg_storage_volume_5_years),
#                 avg_storage_volume_20_years   = VALUES(avg_storage_volume_20_years),
#                 avg_percentage_full_12_months = VALUES(avg_percentage_full_12_months),
#                 avg_percentage_full_5_years   = VALUES(avg_percentage_full_5_years),
#                 avg_percentage_full_20_years  = VALUES(avg_percentage_full_20_years),
#                 avg_storage_inflow_12_months  = VALUES(avg_storage_inflow_12_months),
#                 avg_storage_inflow_5_years    = VALUES(avg_storage_inflow_5_years),
#                 avg_storage_inflow_20_years   = VALUES(avg_storage_inflow_20_years),
#                 avg_storage_release_12_months = VALUES(avg_storage_release_12_months),
#                 avg_storage_release_5_years   = VALUES(avg_storage_release_5_years),
#                 avg_storage_release_20_years  = VALUES(avg_storage_release_20_years)
#         """)

#         with engine.connect() as connection:
#             logger.info("Database connection successful!")

#             dam_ids = connection.execute(text("SELECT dam_id FROM dams")).scalars().all()
#             if not dam_ids:
#                 logger.info("No dams found. Exiting.")
#                 return

#             logger.info(
#                 "Seeding specific_dam_analysis for %d dam(s) with analysis_date=%s",
#                 len(dam_ids), analysis_date.isoformat()
#             )

#             def pick(primary_val: Any, latest_row: Optional[Mapping[str, Any]], latest_key: str):
#                 if primary_val is not None:
#                     return primary_val
#                 if latest_row is None:
#                     return None
#                 return latest_row.get(latest_key)

#             for idx, dam_id in enumerate(dam_ids, start=1):
#                 row_12  = connection.execute(avg_window_sql(12),  {"dam_id": dam_id}).mappings().fetchone()
#                 row_60  = connection.execute(avg_window_sql(60),  {"dam_id": dam_id}).mappings().fetchone()
#                 row_240 = connection.execute(avg_window_sql(240), {"dam_id": dam_id}).mappings().fetchone()
#                 latest  = connection.execute(latest_sql, {"dam_id": dam_id}).mappings().fetchone()

#                 avg_vol_12  = row_12["avg_storage_volume"]   if row_12  else None
#                 avg_vol_60  = row_60["avg_storage_volume"]   if row_60  else None
#                 avg_vol_240 = row_240["avg_storage_volume"]  if row_240 else None

#                 avg_pct_12  = row_12["avg_percentage_full"]  if row_12  else None
#                 avg_pct_60  = row_60["avg_percentage_full"]  if row_60  else None
#                 avg_pct_240 = row_240["avg_percentage_full"] if row_240 else None

#                 avg_in_12   = row_12["avg_storage_inflow"]   if row_12  else None
#                 avg_in_60   = row_60["avg_storage_inflow"]   if row_60  else None
#                 avg_in_240  = row_240["avg_storage_inflow"]  if row_240 else None

#                 avg_out_12  = row_12["avg_storage_release"]  if row_12  else None
#                 avg_out_60  = row_60["avg_storage_release"]  if row_60  else None
#                 avg_out_240 = row_240["avg_storage_release"] if row_240 else None

#                 params = {
#                     "dam_id": dam_id,
#                     "analysis_date": analysis_date,

#                     "avg_vol_12":  pick(avg_vol_12,  latest, "latest_storage_volume"),
#                     "avg_vol_60":  pick(avg_vol_60,  latest, "latest_storage_volume"),
#                     "avg_vol_240": pick(avg_vol_240, latest, "latest_storage_volume"),

#                     "avg_pct_12":  pick(avg_pct_12,  latest, "latest_percentage_full"),
#                     "avg_pct_60":  pick(avg_pct_60,  latest, "latest_percentage_full"),
#                     "avg_pct_240": pick(avg_pct_240, latest, "latest_percentage_full"),

#                     "avg_in_12":   pick(avg_in_12,   latest, "latest_storage_inflow"),
#                     "avg_in_60":   pick(avg_in_60,   latest, "latest_storage_inflow"),
#                     "avg_in_240":  pick(avg_in_240,  latest, "latest_storage_inflow"),

#                     "avg_out_12":  pick(avg_out_12,  latest, "latest_storage_release"),
#                     "avg_out_60":  pick(avg_out_60,  latest, "latest_storage_release"),
#                     "avg_out_240": pick(avg_out_240, latest, "latest_storage_release"),
#                 }

#                 connection.execute(upsert_sql, params)

#                 if idx % 25 == 0 or idx == len(dam_ids):
#                     logger.info("Processed %d/%d dams...", idx, len(dam_ids))

#             logger.info("Data successfully inserted/updated in specific_dam_analysis.")

#     except Exception as e:
#         logger.error(f"An error occurred: {e}")

# if __name__ == "__main__":
#     insert_specific_dam_analysis_data()
