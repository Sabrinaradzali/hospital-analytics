
# Hospital Operations Analytics Dashboard

## Project Overview

This project focuses on building a hospital operations analytics workflow using synthetic healthcare data. The objective is to demonstrate data cleaning, SQL-based analysis, KPI development, and Power BI dashboard creation to support operational monitoring and data-driven decision-making.

The project covers the preparation of structured healthcare data and the development of an interactive dashboard for monitoring encounter volume, emergency activity, inpatient activity, and data quality review records.

> **Data Disclaimer:** This project uses synthetic healthcare data. It does not contain real patient information or represent actual operational data. Operational definitions and analytical thresholds are illustrative and intended for portfolio demonstration purposes.

## Project Objectives

- Prepare and clean healthcare-related datasets.
- Store structured data in a SQLite database.
- Use SQL to develop operational KPI views.
- Identify data quality review records.
- Export KPI datasets for dashboard development.
- Build an interactive Power BI dashboard.
- Demonstrate a structured approach to data preparation and reporting.

## Tools and Technologies

- **Python:** Data cleaning, transformation, and KPI preparation
- **Pandas:** Data manipulation and preprocessing
- **SQLite:** Data storage and SQL analysis
- **SQL:** KPI views and operational analysis
- **Power BI Desktop:** Dashboard development and visualization
- **GitHub:** Project documentation and version control

## Data Sources

The project uses synthetic healthcare datasets generated using Synthea.

The datasets include:

- Patients
- Encounters
- Observations
- Procedures
- Medications
- Conditions
- Organizations
- Payers

The analysis focuses on encounter-related operational metrics and selected data quality indicators.

## Data Processing Workflow

1. Obtain synthetic healthcare datasets.
2. Inspect the structure and quality of the raw data.
3. Clean and standardize relevant datasets using Python.
4. Store cleaned datasets in SQLite.
5. Create SQL views for monthly operational KPIs.
6. Export KPI results into CSV files.
7. Import the KPI dataset into Power BI.
8. Develop an interactive dashboard.

## Key Performance Indicators

The dashboard currently includes:

- **Total Encounters:** Total number of encounters within the selected analytical dataset.
- **Emergency Encounters:** Number of emergency encounter records.
- **Inpatient Encounters:** Number of inpatient encounter records.
- **Quality Review Records:** Records identified for additional data quality review.
- **Monthly Encounter Trend:** Monthly changes in encounter volume.
- **Date Range Slicer:** Allows users to filter the dashboard by encounter date.

## Power BI Dashboard

The dashboard provides an overview of encounter-related operational metrics through:

- KPI cards
- Monthly encounter trend chart
- Date range slicer
- Dashboard title and explanatory description

The dashboard is designed as a portfolio demonstration of healthcare operations reporting and KPI monitoring.

## Data Quality Review

A quality review indicator was developed to identify encounter records requiring additional review based on the project's duration-related rule.

The quality review metric is intended to demonstrate how data quality checks can be incorporated into an operational analytics workflow.

The review results should not be interpreted as clinical findings or real hospital performance indicators.

## Project Structure

```text
hospital-analytics/
│
├── data/
│   ├── cleaned/
│   ├── database/
│   └── kpi/
│
├── docs/
│
├── python/
│   ├── inspect_data.py
│   ├── clean_patients.py
│   ├── clean_encounters.py
│   ├── clean_observations.py
│   ├── clean_procedures.py
│   ├── clean_medications.py
│   ├── clean_conditions.py
│   ├── clean_organizations.py
│   ├── clean_payers.py
│   ├── kpi_encounters.py
│   ├── kpi_monthly.py
│   ├── load_sqlite.py
│   └── export_kpis.py
│
├── sql/
│   ├── encounter_analysis.sql
│   ├── monthly_encounter_analysis.sql
│   ├── monthly_operational_kpis.sql
│   └── dashboard_monthly_kpis.sql
│
├── Hospital_Operations_Analytics.pbix
└── README.md
```

## Scope and Limitations

- The dataset is synthetic and does not represent actual hospital operations.
- KPI definitions are designed for portfolio demonstration.
- The dashboard focuses on selected encounter-related indicators.
- The current analysis uses an explicitly selected analytical date range.
- The results should not be used for clinical, financial, or operational decisions in a real healthcare organization.

## Future Improvements

- Add department-level operational analysis.
- Add patient flow and length-of-stay metrics.
- Develop additional data quality checks.
- Add SQL validation queries and automated testing.
- Improve dashboard layout and visual formatting.
- Add drill-through pages for detailed analysis.
- Introduce role-based access and governance documentation.
- Publish a documented KPI dictionary.

## Author

Nur Sabrina Radzali

Computer and Communication Systems Engineering Graduate

Universiti Putra Malaysia