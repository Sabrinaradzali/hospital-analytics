
import pandas as pd
from pathlib import Path

# Project and data directories
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

# Load observations data
observations_path = DATA_DIR / "observations.csv"

observations_df = pd.read_csv(observations_path)

# Keep vital-sign observations for the initial analytical dataset
vital_signs = [
    "Body Height",
    "Body Weight",
    "Body mass index (BMI) [Ratio]",
    "Systolic Blood Pressure",
    "Diastolic Blood Pressure",
    "Heart rate",
    "Respiratory rate",
]

observations_clean = observations_df[
    observations_df["DESCRIPTION"].isin(vital_signs)
].copy()

# Select relevant columns
selected_columns = [
    "DATE",
    "PATIENT",
    "ENCOUNTER",
    "CATEGORY",
    "CODE",
    "DESCRIPTION",
    "VALUE",
    "UNITS",
    "TYPE",
]

observations_clean = observations_clean[selected_columns]

# Convert the date column
observations_clean["DATE"] = pd.to_datetime(
    observations_clean["DATE"],
    errors="coerce",
    utc=True
)

# Convert values to numeric where possible
observations_clean["VALUE_NUMERIC"] = pd.to_numeric(
    observations_clean["VALUE"],
    errors="coerce"
)

# Create data-quality flags
observations_clean["QUALITY_FLAG"] = "Valid"

observations_clean.loc[
    observations_clean["VALUE_NUMERIC"].isna(),
    "QUALITY_FLAG"
] = "Non-numeric value"

observations_clean.loc[
    observations_clean["PATIENT"].isna(),
    "QUALITY_FLAG"
] = "Missing patient ID"

# Display results
print("=" * 60)
print("CLEANED OBSERVATIONS DATA")
print("=" * 60)

print("\nNumber of rows:", len(observations_clean))

print("\nObservation descriptions:")
print(observations_clean["DESCRIPTION"].value_counts())

print("\nMissing values:")
print(observations_clean.isnull().sum())

print("\nQuality flag distribution:")
print(observations_clean["QUALITY_FLAG"].value_counts())

# Save the cleaned dataset
output_path = DATA_DIR / "cleaned" / "observations_clean.csv"
observations_clean.to_csv(output_path, index=False)

print("\nCleaned dataset saved to:")
print(output_path)