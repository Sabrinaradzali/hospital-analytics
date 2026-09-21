import pandas as pd
from pathlib import Path

# Define project directories
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

# Load medications data
medications_path = DATA_DIR / "medications.csv"
medications_df = pd.read_csv(medications_path)

# Select relevant columns
selected_columns = [
    "START",
    "STOP",
    "PATIENT",
    "PAYER",
    "ENCOUNTER",
    "CODE",
    "DESCRIPTION",
    "BASE_COST",
    "PAYER_COVERAGE",
    "DISPENSES",
    "TOTALCOST",
    "REASONCODE",
    "REASONDESCRIPTION",
]

medications_clean = medications_df[selected_columns].copy()

# Convert date columns
medications_clean["START"] = pd.to_datetime(
    medications_clean["START"],
    errors="coerce",
    utc=True
)

medications_clean["STOP"] = pd.to_datetime(
    medications_clean["STOP"],
    errors="coerce",
    utc=True
)

# Calculate medication duration in days
medications_clean["DURATION_DAYS"] = (
    medications_clean["STOP"] - medications_clean["START"]
).dt.total_seconds() / (60 * 60 * 24)

# Convert numeric columns
numeric_columns = [
    "BASE_COST",
    "PAYER_COVERAGE",
    "DISPENSES",
    "TOTALCOST",
]

for column in numeric_columns:
    medications_clean[column] = pd.to_numeric(
        medications_clean[column],
        errors="coerce"
    )

# Create quality flags
medications_clean["QUALITY_FLAG"] = "Valid"

medications_clean.loc[
    medications_clean["STOP"].isna(),
    "QUALITY_FLAG"
] = "Missing stop date"

medications_clean.loc[
    medications_clean["DURATION_DAYS"] < 0,
    "QUALITY_FLAG"
] = "Invalid negative duration"

medications_clean.loc[
    medications_clean["PATIENT"].isna(),
    "QUALITY_FLAG"
] = "Missing patient ID"

medications_clean.loc[
    medications_clean["TOTALCOST"].isna(),
    "QUALITY_FLAG"
] = "Missing total cost"

# Display results
print("=" * 60)
print("CLEANED MEDICATIONS DATA")
print("=" * 60)

print("\nNumber of rows:", len(medications_clean))

print("\nMedication descriptions:")
print(
    medications_clean["DESCRIPTION"]
    .value_counts()
    .head(20)
)

print("\nMissing values:")
print(medications_clean.isnull().sum())

print("\nDuration summary:")
print(medications_clean["DURATION_DAYS"].describe())

print("\nQuality flag distribution:")
print(medications_clean["QUALITY_FLAG"].value_counts())

print("\nTotal cost summary:")
print(medications_clean["TOTALCOST"].describe())

# Save cleaned dataset
output_path = DATA_DIR / "cleaned" / "medications_clean.csv"

medications_clean.to_csv(
    output_path,
    index=False
)

print("\nCleaned dataset saved to:")
print(output_path)