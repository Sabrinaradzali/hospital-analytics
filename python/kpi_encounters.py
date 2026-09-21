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
# 3. Prepare duration data
# -----------------------------
encounters["DURATION_MINUTES"] = pd.to_numeric(
    encounters["DURATION_MINUTES"],
    errors="coerce"
)


# -----------------------------
# 4. Calculate overall KPIs
# -----------------------------
total_encounters = len(encounters)

average_duration = encounters["DURATION_MINUTES"].mean()

emergency_encounters = (
    encounters["ENCOUNTERCLASS"] == "emergency"
).sum()

inpatient_encounters = (
    encounters["ENCOUNTERCLASS"] == "inpatient"
).sum()

quality_issues = (
    encounters["DURATION_QUALITY_FLAG"] != "Valid"
).sum()


kpi_summary = pd.DataFrame({
    "KPI": [
        "Total Encounters",
        "Average Duration (Minutes)",
        "Emergency Encounters",
        "Inpatient Encounters",
        "Records Requiring Quality Review"
    ],
    "VALUE": [
        total_encounters,
        round(average_duration, 2),
        emergency_encounters,
        inpatient_encounters,
        quality_issues
    ]
})


# -----------------------------
# 5. Calculate encounters by type
# -----------------------------
encounters_by_type = (
    encounters["ENCOUNTERCLASS"]
    .value_counts()
    .reset_index()
)

encounters_by_type.columns = [
    "ENCOUNTER_CLASS",
    "ENCOUNTER_COUNT"
]


# -----------------------------
# 6. Calculate duration by type
# -----------------------------
duration_by_type = (
    encounters
    .groupby("ENCOUNTERCLASS")["DURATION_MINUTES"]
    .agg(
        TOTAL_ENCOUNTERS="count",
        AVERAGE_DURATION_MINUTES="mean",
        MEDIAN_DURATION_MINUTES="median"
    )
    .reset_index()
)

duration_by_type["AVERAGE_DURATION_MINUTES"] = (
    duration_by_type["AVERAGE_DURATION_MINUTES"].round(2)
)

duration_by_type["MEDIAN_DURATION_MINUTES"] = (
    duration_by_type["MEDIAN_DURATION_MINUTES"].round(2)
)


# -----------------------------
# 7. Save KPI files
# -----------------------------
kpi_summary.to_csv(
    OUTPUT_DIR / "encounter_kpi_summary.csv",
    index=False
)

encounters_by_type.to_csv(
    OUTPUT_DIR / "encounters_by_type.csv",
    index=False
)

duration_by_type.to_csv(
    OUTPUT_DIR / "duration_by_type.csv",
    index=False
)


# -----------------------------
# 8. Display results
# -----------------------------
print("\nKPI SUMMARY")
print(kpi_summary.to_string(index=False))

print("\nENCOUNTERS BY TYPE")
print(encounters_by_type.to_string(index=False))

print("\nDURATION BY TYPE")
print(duration_by_type.to_string(index=False))

print("\nKPI files saved successfully.")