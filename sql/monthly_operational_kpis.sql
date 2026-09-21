-- Monthly operational KPI view

DROP VIEW IF EXISTS monthly_operational_kpis;

CREATE VIEW monthly_operational_kpis AS
SELECT
    strftime('%Y-%m', START) AS ENCOUNTER_MONTH,

    COUNT(*) AS TOTAL_ENCOUNTERS,

    SUM(
        CASE
            WHEN ENCOUNTERCLASS = 'emergency' THEN 1
            ELSE 0
        END
    ) AS EMERGENCY_ENCOUNTERS,

    SUM(
        CASE
            WHEN ENCOUNTERCLASS = 'inpatient' THEN 1
            ELSE 0
        END
    ) AS INPATIENT_ENCOUNTERS,

    SUM(
        CASE
            WHEN DURATION_QUALITY_FLAG != 'Valid' THEN 1
            ELSE 0
        END
    ) AS QUALITY_REVIEW_RECORDS

FROM encounters
GROUP BY ENCOUNTER_MONTH
ORDER BY ENCOUNTER_MONTH;