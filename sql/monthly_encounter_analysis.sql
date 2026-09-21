-- Reusable monthly encounter summary view

DROP VIEW IF EXISTS monthly_encounter_summary;

CREATE VIEW monthly_encounter_summary AS
SELECT
    strftime('%Y-%m', START) AS ENCOUNTER_MONTH,
    COUNT(*) AS TOTAL_ENCOUNTERS
FROM encounters
GROUP BY ENCOUNTER_MONTH
ORDER BY ENCOUNTER_MONTH;