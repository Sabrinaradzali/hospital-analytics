import pandas as pd
from pathlib import Path

# Define project directories
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

# Load payers data
payers_path = DATA_DIR / "payers.csv"
payers_df = pd.read_csv(payers_path)

# Select relevant operational and financial columns
selected_columns = [
    "Id",
    "NAME",
    "OWNERSHIP",
    "AMOUNT_COVERED",
    "AMOUNT_UNCOVERED",
    "REVENUE",
    "COVERED_ENCOUNTERS",
    "UNCOVERED_ENCOUNTERS",
    "COVERED_MEDICATIONS",
    "UNCOVERED_MEDICATIONS",
    "COVERED_PROCEDURES",
    "UNCOVERED_PROCEDURES",
    "COVERED_IMMUNIZATIONS",
    "UNCOVERED_IMMUNIZATIONS",
    "UNIQUE_CUSTOMERS",
    "QOLS_AVG",
    "MEMBER_MONTHS",
]

payers_clean = payers_df[selected_columns].copy()

# Convert numeric columns
numeric_columns = [
    "AMOUNT_COVERED",
    "AMOUNT_UNCOVERED",
    "REVENUE",
    "COVERED_ENCOUNTERS",
    "UNCOVERED_ENCOUNTERS",
    "COVERED_MEDICATIONS",
    "UNCOVERED_MEDICATIONS",
    "COVERED_PROCEDURES",
    "UNCOVERED_PROCEDURES",
    "COVERED_IMMUNIZATIONS",
    "UNCOVERED_IMMUNIZATIONS",
    "UNIQUE_CUSTOMERS",
    "QOLS_AVG",
    "MEMBER_MONTHS",
]

for column in numeric_columns:
    payers_clean[column] = pd.to_numeric(
        payers_clean[column],
        errors="coerce"
    )

# Create quality flags
payers_clean["QUALITY_FLAG"] = "Valid"

payers_clean.loc[
    payers_clean["NAME"].isna(),
    "QUALITY_FLAG"
] = "Missing payer name"

payers_clean.loc[
    payers_clean["AMOUNT_COVERED"] < 0,
    "QUALITY_FLAG"
] = "Invalid negative covered amount"

payers_clean.loc[
    payers_clean["AMOUNT_UNCOVERED"] < 0,
    "QUALITY_FLAG"
] = "Invalid negative uncovered amount"

payers_clean.loc[
    payers_clean["UNIQUE_CUSTOMERS"] < 0,
    "QUALITY_FLAG"
] = "Invalid negative customer count"

payers_clean.loc[
    payers_clean["MEMBER_MONTHS"] < 0,
    "QUALITY_FLAG"
] = "Invalid negative member months"

# Display results
print("=" * 60)
print("CLEANED PAYERS DATA")
print("=" * 60)

print("\nNumber of rows:", len(payers_clean))

print("\nMissing values:")
print(payers_clean.isnull().sum())

print("\nQuality flag distribution:")
print(payers_clean["QUALITY_FLAG"].value_counts())

print("\nCoverage summary:")
print(
    payers_clean[
        [
            "AMOUNT_COVERED",
            "AMOUNT_UNCOVERED",
            "COVERED_ENCOUNTERS",
            "UNCOVERED_ENCOUNTERS",
        ]
    ].describe()
)

print("\nRevenue summary:")
print(payers_clean["REVENUE"].describe())

# Save cleaned dataset
output_path = DATA_DIR / "cleaned" / "payers_clean.csv"

payers_clean.to_csv(
    output_path,
    index=False
)

print("\nCleaned dataset saved to:")
print(output_path)