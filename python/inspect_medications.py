import pandas as pd
from pathlib import Path

# Define project directories
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

# Load medications data
medications_path = DATA_DIR / "medications.csv"
medications_df = pd.read_csv(medications_path)

print("=" * 60)
print("MEDICATIONS DATA INSPECTION")
print("=" * 60)

print("\nShape:")
print(medications_df.shape)

print("\nColumns:")
print(medications_df.columns.tolist())

print("\nFirst 5 rows:")
print(medications_df.head())

print("\nMissing values:")
print(medications_df.isnull().sum())

print("\nMedication descriptions:")
print(medications_df["DESCRIPTION"].value_counts().head(20))