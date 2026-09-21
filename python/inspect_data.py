
import pandas as pd
from pathlib import Path

# Find the project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

# CSV files we want to inspect
files = [
    "patients.csv",
    "encounters.csv",
    "observations.csv",
    "procedures.csv",
    "medications.csv",
    "conditions.csv",
    "organizations.csv",
    "payers.csv",
]

print("=" * 60)
print("HOSPITAL DATA INSPECTION")
print("=" * 60)

for filename in files:
    file_path = DATA_DIR / filename

    print(f"\n{'-' * 60}")
    print(f"File: {filename}")

    if not file_path.exists():
        print("Status: File not found")
        continue

    df = pd.read_csv(file_path, nrows=5)

    print(f"Columns: {len(df.columns)}")
    print(f"Column names: {list(df.columns)}")

    print("Status: Successfully loaded")

    
# Detailed inspection of patients.csv
print("\n" + "=" * 60)
print("PATIENTS DATA PREVIEW")
print("=" * 60)

patients_path = DATA_DIR / "patients.csv"
patients_df = pd.read_csv(patients_path, nrows=5)

print("\nFirst 5 rows:")
print(patients_df.to_string(index=False))

print("\nData types:")
print(patients_df.dtypes)

print("\nMissing values in first 5 rows:")
print(patients_df.isnull().sum())