
import pandas as pd
from pathlib import Path

# Project and data directories
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

# Load encounters data
encounters_path = DATA_DIR / "encounters.csv"
encounters_df = pd.read_csv(encounters_path)

# Select relevant columns for operational analytics
selected_columns = [
    "Id",
    "START",
    "STOP",
    "PATIENT",
    "ORGANIZATION",
    "PAYER",
    "ENCOUNTERCLASS",
    "CODE",
    "DESCRIPTION",
    "BASE_ENCOUNTER_COST",
    "TOTAL_CLAIM_COST",
    "PAYER_COVERAGE",
    "REASONCODE",
    "REASONDESCRIPTION",
]

encounters_clean = encounters_df[selected_columns].copy()

# Convert date columns to datetime
encounters_clean["START"] = pd.to_datetime(
    encounters_clean["START"],
    errors="coerce",
    utc=True
)

encounters_clean["STOP"] = pd.to_datetime(
    encounters_clean["STOP"],
    errors="coerce",
    utc=True
)

# Calculate encounter duration in minutes
encounters_clean["DURATION_MINUTES"] = (
    encounters_clean["STOP"] - encounters_clean["START"]
).dt.total_seconds() / 60

# Display the cleaned structure
print("=" * 60)
print("CLEANED ENCOUNTERS DATA")
print("=" * 60)

print("\nNumber of rows:", len(encounters_clean))

print("\nData types:")
print(encounters_clean.dtypes)

print("\nMissing values:")
print(encounters_clean.isnull().sum())

print("\nEncounter duration summary:")
print(encounters_clean["DURATION_MINUTES"].describe())

# Save the cleaned dataset
output_path = DATA_DIR / "cleaned" / "encounters_clean.csv"
encounters_clean.to_csv(output_path, index=False)

print("\nCleaned dataset saved to:")
print(output_path)

# Analyze encounter duration by encounter class
print("\n" + "=" * 60)
print("DURATION BY ENCOUNTER CLASS")
print("=" * 60)

duration_summary = (
    encounters_clean
    .groupby("ENCOUNTERCLASS")["DURATION_MINUTES"]
    .describe()
    .round(2)
)

print(duration_summary)

# Inspect the 20 longest encounters
print("\n" + "=" * 60)
print("20 LONGEST ENCOUNTERS")
print("=" * 60)

longest_encounters = (
    encounters_clean[
        [
            "Id",
            "PATIENT",
            "ENCOUNTERCLASS",
            "START",
            "STOP",
            "DURATION_MINUTES",
            "DESCRIPTION",
        ]
    ]
    .sort_values("DURATION_MINUTES", ascending=False)
    .head(20)
)

print(longest_encounters.to_string(index=False))


# Create data-quality flags for encounter duration
print("\n" + "=" * 60)
print("DURATION QUALITY CHECKS")
print("=" * 60)

# Flag records with invalid or unusually long durations
encounters_clean["DURATION_QUALITY_FLAG"] = "Valid"

encounters_clean.loc[
    encounters_clean["DURATION_MINUTES"] < 0,
    "DURATION_QUALITY_FLAG"
] = "Invalid negative duration"

encounters_clean.loc[
    (
        (encounters_clean["DURATION_MINUTES"] > 1440)
        & (~encounters_clean["ENCOUNTERCLASS"].isin(["inpatient", "hospice", "snf"]))
    ),
    "DURATION_QUALITY_FLAG"
] = "Review: extended duration"

print("\nQuality flag distribution:")
print(encounters_clean["DURATION_QUALITY_FLAG"].value_counts())

print("\nExtended-duration records by encounter class:")
print(
    encounters_clean[
        encounters_clean["DURATION_QUALITY_FLAG"] == "Review: extended duration"
    ]["ENCOUNTERCLASS"].value_counts()
)

# Save the dataset with quality flags
encounters_clean.to_csv(output_path, index=False)

print("\nUpdated encounters dataset saved to:")
print(output_path)
