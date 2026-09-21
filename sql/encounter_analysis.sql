@"
-- Encounter count by encounter type

SELECT
    ENCOUNTERCLASS,
    COUNT(*) AS ENCOUNTER_COUNT
FROM encounters
GROUP BY ENCOUNTERCLASS
ORDER BY ENCOUNTER_COUNT DESC;
"@ | Set-Content sql\encounter_analysis.sql