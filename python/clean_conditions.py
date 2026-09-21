import pandas as pd
from pathlib import Path

# Define project directories
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

# Load conditions data
conditions_path = DATA_DIR / "conditions.csv"
conditions_df = pd.read_csv(conditions_path)

# Select relevant columns
selected_columns = [
    "START",
    "STOP",
    "PATIENT",
    "ENCOUNTER",
    "SYSTEM",
    "CODE",
    "DESCRIPTION",
]

conditions_clean = conditions_df[selected_columns].copy()

# Convert date columns
conditions_clean["START"] = pd.to_datetime(
    conditions_clean["START"],
    errors="coerce",
    utc=True
)

conditions_clean["STOP"] = pd.to_datetime(
    conditions_clean["STOP"],
    errors="coerce",
    utc=True
)

# Calculate condition duration in days
conditions_clean["DURATION_DAYS"] = (
    conditions_clean["STOP"] - conditions_clean["START"]
).dt.total_seconds() / (60 * 60 * 24)

# Create quality flags
conditions_clean["QUALITY_FLAG"] = "Valid"

conditions_clean.loc[
    conditions_clean["START"].isna(),
    "QUALITY_FLAG"
] = "Missing or invalid start date"

conditions_clean.loc[
    conditions_clean["DURATION_DAYS"] < 0,
    "QUALITY_FLAG"
] = "Invalid negative duration"

conditions_clean.loc[
    conditions_clean["PATIENT"].isna(),
    "QUALITY_FLAG"
] = "Missing patient ID"

# Display results
print("=" * 60)
print("CLEANED CONDITIONS DATA")
print("=" * 60)

print("\nNumber of rows:", len(conditions_clean))

print("\nCondition descriptions:")
print(
    conditions_clean["DESCRIPTION"]
    .value_counts()
    .head(20)
)

print("\nMissing values:")
print(conditions_clean.isnull().sum())

print("\nDuration summary:")
print(conditions_clean["DURATION_DAYS"].describe())

print("\nQuality flag distribution:")
print(conditions_clean["QUALITY_FLAG"].value_counts())

# Save cleaned dataset
output_path = DATA_DIR / "cleaned" / "conditions_clean.csv"

conditions_clean.to_csv(
    output_path,
    index=False
)

print("\nCleaned dataset saved to:")
print(output_path)