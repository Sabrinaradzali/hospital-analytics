import pandas as pd
from pathlib import Path

# Define project directories
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

# Load procedures data
procedures_path = DATA_DIR / "procedures.csv"
procedures_df = pd.read_csv(procedures_path)

# Select relevant columns
selected_columns = [
    "START",
    "STOP",
    "PATIENT",
    "ENCOUNTER",
    "SYSTEM",
    "CODE",
    "DESCRIPTION",
    "BASE_COST",
    "REASONCODE",
    "REASONDESCRIPTION",
]

procedures_clean = procedures_df[selected_columns].copy()

# Convert date columns
procedures_clean["START"] = pd.to_datetime(
    procedures_clean["START"],
    errors="coerce",
    utc=True
)

procedures_clean["STOP"] = pd.to_datetime(
    procedures_clean["STOP"],
    errors="coerce",
    utc=True
)

# Calculate procedure duration in minutes
procedures_clean["DURATION_MINUTES"] = (
    procedures_clean["STOP"] - procedures_clean["START"]
).dt.total_seconds() / 60

# Convert base cost to numeric
procedures_clean["BASE_COST"] = pd.to_numeric(
    procedures_clean["BASE_COST"],
    errors="coerce"
)

# Create quality flags
procedures_clean["QUALITY_FLAG"] = "Valid"

procedures_clean.loc[
    procedures_clean["START"].isna()
    | procedures_clean["STOP"].isna(),
    "QUALITY_FLAG"
] = "Missing or invalid date"

procedures_clean.loc[
    procedures_clean["DURATION_MINUTES"] < 0,
    "QUALITY_FLAG"
] = "Invalid negative duration"

procedures_clean.loc[
    procedures_clean["PATIENT"].isna(),
    "QUALITY_FLAG"
] = "Missing patient ID"

procedures_clean.loc[
    procedures_clean["BASE_COST"].isna(),
    "QUALITY_FLAG"
] = "Missing or invalid cost"

# Display results
print("=" * 60)
print("CLEANED PROCEDURES DATA")
print("=" * 60)

print("\nNumber of rows:", len(procedures_clean))

print("\nProcedure descriptions:")
print(procedures_clean["DESCRIPTION"].value_counts().head(20))

print("\nMissing values:")
print(procedures_clean.isnull().sum())

print("\nDuration summary:")
print(procedures_clean["DURATION_MINUTES"].describe())

print("\nQuality flag distribution:")
print(procedures_clean["QUALITY_FLAG"].value_counts())

print("\nBase cost summary:")
print(procedures_clean["BASE_COST"].describe())

# Save cleaned dataset
output_path = DATA_DIR / "cleaned" / "procedures_clean.csv"

procedures_clean.to_csv(
    output_path,
    index=False
)

print("\nCleaned dataset saved to:")
print(output_path)