import pandas as pd
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

procedures_path = DATA_DIR / "procedures.csv"

procedures_df = pd.read_csv(procedures_path)

print("=" * 60)
print("PROCEDURES DATA INSPECTION")
print("=" * 60)

print("\nShape:")
print(procedures_df.shape)

print("\nColumns:")
print(procedures_df.columns.tolist())

print("\nFirst 5 rows:")
print(procedures_df.head())

print("\nMissing values:")
print(procedures_df.isnull().sum())

print("\nProcedure descriptions:")
print(procedures_df["DESCRIPTION"].value_counts().head(20))