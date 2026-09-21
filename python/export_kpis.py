
from pathlib import Path
import sqlite3
import pandas as pd


# Project folders
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_DIR = BASE_DIR / "data" / "database"
KPI_DIR = BASE_DIR / "data" / "kpi"

KPI_DIR.mkdir(parents=True, exist_ok=True)

DB_PATH = DATABASE_DIR / "hospital_analytics.db"
OUTPUT_PATH = KPI_DIR / "monthly_operational_kpis.csv"


# Connect to SQLite database
with sqlite3.connect(DB_PATH) as connection:

    query = """
    SELECT *
    FROM dashboard_monthly_kpis
    ORDER BY ENCOUNTER_MONTH;
    """

    df = pd.read_sql_query(query, connection)


# Export results to CSV
df.to_csv(OUTPUT_PATH, index=False)

print("KPI export completed successfully.")
print(f"Rows exported: {len(df):,}")
print(f"Saved to: {OUTPUT_PATH}")