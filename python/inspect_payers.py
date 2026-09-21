import pandas as pd
from pathlib import Path

# Define project directories
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

# Load payers data
payers_path = DATA_DIR / "payers.csv"
payers_df = pd.read_csv(payers_path)

print("=" * 60)
print("PAYERS DATA INSPECTION")
print("=" * 60)

print("\nShape:")
print(payers_df.shape)

print("\nColumns:")
print(payers_df.columns.tolist())

print("\nFirst 5 rows:")
print(payers_df.head())

print("\nMissing values:")
print(payers_df.isnull().sum())
