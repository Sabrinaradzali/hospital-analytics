import pandas as pd
from pathlib import Path


# -----------------------------
# 1. Define file paths
# -----------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = PROJECT_ROOT / "data" / "cleaned" / "encounters_clean.csv"
OUTPUT_DIR = PROJECT_ROOT / "data" / "kpi"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# -----------------------------
# 2. Load cleaned encounters
# -----------------------------
encounters = pd.read_csv(INPUT_FILE)

print("Encounters loaded successfully.")
print(f"Total records: {len(encounters):,}")


# -----------------------------
# 3. Convert date column
# -----------------------------
encounters["START"] = pd.to_datetime(
    encounters["START"],
    errors="coerce",
    utc=True
)

encounters["MONTH"] = encounters["START"].dt.to_period("M").astype(str)


# -----------------------------
# 4. Calculate monthly KPIs
# -----------------------------
monthly_kpis = (
    encounters
    .groupby("MONTH")
    .agg(
        TOTAL_ENCOUNTERS=("Id", "count"),
        AVERAGE_DURATION_MINUTES=("DURATION_MINUTES", "mean"),
        EMERGENCY_ENCOUNTERS=(
            "ENCOUNTERCLASS",
            lambda x: (x == "emergency").sum()
        ),
        INPATIENT_ENCOUNTERS=(
            "ENCOUNTERCLASS",
            lambda x: (x == "inpatient").sum()
        ),
        QUALITY_REVIEW_RECORDS=(
            "DURATION_QUALITY_FLAG",
            lambda x: (x != "Valid").sum()
        )
    )
    .reset_index()
)


# -----------------------------
# 5. Round numeric values
# -----------------------------
monthly_kpis["AVERAGE_DURATION_MINUTES"] = (
    monthly_kpis["AVERAGE_DURATION_MINUTES"].round(2)
)


# -----------------------------
# 6. Sort by month
# -----------------------------
monthly_kpis = monthly_kpis.sort_values("MONTH")


# -----------------------------
# 7. Save monthly KPI file
# -----------------------------
output_file = OUTPUT_DIR / "monthly_encounter_kpis.csv"

monthly_kpis.to_csv(
    output_file,
    index=False
)


# -----------------------------
# 8. Display results
# -----------------------------
print("\nMONTHLY ENCOUNTER KPIs")
print(monthly_kpis.to_string(index=False))

print(f"\nMonthly KPI file saved to: {output_file}")