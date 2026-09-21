
import pandas as pd
from pathlib import Path

# Project and data directories
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data"

# Load observations data
observations_path = DATA_DIR / "observations.csv"

observations_df = pd.read_csv(
    observations_path,
    usecols=[
        "DATE",
        "PATIENT",
        "ENCOUNTER",
        "CATEGORY",
        "CODE",
        "DESCRIPTION",
        "VALUE",
        "UNITS",
        "TYPE",
    ],
)

print("=" * 60)
print("OBSERVATIONS DATA INSPECTION")
print("=" * 60)

print("\nNumber of rows:", len(observations_df))
print("Number of columns:", len(observations_df.columns))

print("\nColumn names:")
print(list(observations_df.columns))

print("\nFirst 5 rows:")
print(observations_df.head().to_string(index=False))

print("\nData types:")
print(observations_df.dtypes)

print("\nMissing values:")
print(observations_df.isnull().sum())

print("\nObservation categories:")
print(observations_df["CATEGORY"].value_counts())

print("\nTop 15 observation descriptions:")
print(observations_df["DESCRIPTION"].value_counts().head(15))