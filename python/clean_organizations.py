import pandas as pd
from pathlib import Path

# Define project directories
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

# Load organizations data
organizations_path = DATA_DIR / "organizations.csv"
organizations_df = pd.read_csv(organizations_path)

# Select relevant operational columns
selected_columns = [
    "Id",
    "NAME",
    "CITY",
    "STATE",
    "ZIP",
    "LAT",
    "LON",
    "REVENUE",
    "UTILIZATION",
]

organizations_clean = organizations_df[selected_columns].copy()

# Convert numeric columns
numeric_columns = [
    "LAT",
    "LON",
    "REVENUE",
    "UTILIZATION",
]

for column in numeric_columns:
    organizations_clean[column] = pd.to_numeric(
        organizations_clean[column],
        errors="coerce"
    )

# Create quality flags
organizations_clean["QUALITY_FLAG"] = "Valid"

organizations_clean.loc[
    organizations_clean["NAME"].isna(),
    "QUALITY_FLAG"
] = "Missing organization name"

organizations_clean.loc[
    organizations_clean["REVENUE"] < 0,
    "QUALITY_FLAG"
] = "Invalid negative revenue"

organizations_clean.loc[
    organizations_clean["UTILIZATION"] < 0,
    "QUALITY_FLAG"
] = "Invalid negative utilization"

# Display results
print("=" * 60)
print("CLEANED ORGANIZATIONS DATA")
print("=" * 60)

print("\nNumber of rows:", len(organizations_clean))

print("\nMissing values:")
print(organizations_clean.isnull().sum())

print("\nQuality flag distribution:")
print(organizations_clean["QUALITY_FLAG"].value_counts())

print("\nRevenue summary:")
print(organizations_clean["REVENUE"].describe())

print("\nUtilization summary:")
print(organizations_clean["UTILIZATION"].describe())

# Save cleaned dataset
output_path = DATA_DIR / "cleaned" / "organizations_clean.csv"

organizations_clean.to_csv(
    output_path,
    index=False
)

print("\nCleaned dataset saved to:")
print(output_path)