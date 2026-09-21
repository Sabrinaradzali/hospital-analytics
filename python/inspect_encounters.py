
import pandas as pd
from pathlib import Path

# Project and data directories
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

# Load encounters data
encounters_path = DATA_DIR / "encounters.csv"
encounters_df = pd.read_csv(encounters_path)

print("=" * 60)
print("ENCOUNTERS DATA INSPECTION")
print("=" * 60)

print("\nNumber of rows:", len(encounters_df))
print("Number of columns:", len(encounters_df.columns))

print("\nColumn names:")
print(list(encounters_df.columns))

print("\nFirst 5 rows:")
print(encounters_df.head().to_string(index=False))

print("\nData types:")
print(encounters_df.dtypes)

print("\nMissing values:")
print(encounters_df.isnull().sum())

print("\nEncounter class distribution:")
print(encounters_df["ENCOUNTERCLASS"].value_counts())

print("\nTop 10 encounter descriptions:")
print(encounters_df["DESCRIPTION"].value_counts().head(10))