import pandas as pd
from pathlib import Path

# Define project directories
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

# Load organizations data
organizations_path = DATA_DIR / "organizations.csv"
organizations_df = pd.read_csv(organizations_path)

print("=" * 60)
print("ORGANIZATIONS DATA INSPECTION")
print("=" * 60)

print("\nShape:")
print(organizations_df.shape)

print("\nColumns:")
print(organizations_df.columns.tolist())

print("\nFirst 5 rows:")
print(organizations_df.head())

print("\nMissing values:")
print(organizations_df.isnull().sum())