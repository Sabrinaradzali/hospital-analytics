
from pathlib import Path
import sqlite3
import pandas as pd


# Project folders
BASE_DIR = Path(__file__).resolve().parent.parent
CLEANED_DIR = BASE_DIR / "data" / "cleaned"
DATABASE_DIR = BASE_DIR / "data" / "database"

DATABASE_DIR.mkdir(parents=True, exist_ok=True)

DB_PATH = DATABASE_DIR / "hospital_analytics.db"


# CSV files to load
tables = {
    "patients": "patients_clean.csv",
    "encounters": "encounters_clean.csv",
    "observations": "observations_clean.csv",
    "procedures": "procedures_clean.csv",
    "medications": "medications_clean.csv",
    "conditions": "conditions_clean.csv",
    "organizations": "organizations_clean.csv",
    "payers": "payers_clean.csv",
}


# Create SQLite database
with sqlite3.connect(DB_PATH) as connection:

    for table_name, file_name in tables.items():

        file_path = CLEANED_DIR / file_name

        if not file_path.exists():
            print(f"Skipped: {file_name} not found")
            continue

        df = pd.read_csv(file_path)

        df.to_sql(
            table_name,
            connection,
            if_exists="replace",
            index=False
        )

        print(f"Loaded {table_name}: {len(df):,} rows")


print(f"\nDatabase created successfully:")
print(DB_PATH)