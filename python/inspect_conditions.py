import pandas as pd
from pathlib import Path

# Define project directories
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

# Load conditions data
conditions_path = DATA_DIR / "conditions.csv"
conditions_df = pd.read_csv(conditions_path)

print("=" * 60)
print("CONDITIONS DATA INSPECTION")
print("=" * 60)

print("\nShape:")
print(conditions_df.shape)

print("\nColumns:")
print(conditions_df.columns.tolist())

print("\nFirst 5 rows:")
print(conditions_df.head())

print("\nMissing values:")
print(conditions_df.isnull().sum())

print("\nCondition descriptions:")
print(
    conditions_df["DESCRIPTION"]
    .value_counts()
    .head(20)
)