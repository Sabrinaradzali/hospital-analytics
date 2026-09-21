
import pandas as pd
from pathlib import Path

# Project and data directories
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

# Load the synthetic patient data
patients_path = DATA_DIR / "patients.csv"
patients_df = pd.read_csv(patients_path)

# Select only the fields needed for operational analytics
selected_columns = [
    "Id",
    "BIRTHDATE",
    "DEATHDATE",
    "MARITAL",
    "RACE",
    "ETHNICITY",
    "GENDER",
    "CITY",
    "STATE",
    "COUNTY",
    "ZIP",
    "HEALTHCARE_EXPENSES",
    "HEALTHCARE_COVERAGE",
    "INCOME",
]

patients_clean = patients_df[selected_columns].copy()

# Convert date fields to datetime
patients_clean["BIRTHDATE"] = pd.to_datetime(
    patients_clean["BIRTHDATE"],
    errors="coerce"
)

patients_clean["DEATHDATE"] = pd.to_datetime(
    patients_clean["DEATHDATE"],
    errors="coerce"
)

# Display the cleaned structure
print("=" * 60)
print("CLEANED PATIENT DATA")
print("=" * 60)

print("\nColumns:")
print(list(patients_clean.columns))

print("\nNumber of rows:", len(patients_clean))

print("\nData types:")
print(patients_clean.dtypes)

print("\nMissing values:")
print(patients_clean.isnull().sum())

# Save the cleaned patient dataset
output_path = DATA_DIR / "cleaned" / "patients_clean.csv"
patients_clean.to_csv(output_path, index=False)

print("\nCleaned dataset saved to:")
print(output_path)