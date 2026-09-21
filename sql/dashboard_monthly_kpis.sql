-- Dashboard-focused monthly KPI view
-- Scope: 2017 onwards
-- 2026 represents a partial year in this dataset

DROP VIEW IF EXISTS dashboard_monthly_kpis;

CREATE VIEW dashboard_monthly_kpis AS
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

WHERE START >= '2017-01-01'

GROUP BY ENCOUNTER_MONTH
ORDER BY ENCOUNTER_MONTH;