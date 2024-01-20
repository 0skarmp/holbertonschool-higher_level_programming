-- SCRIPT

SELECT state, AVG(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state LIMIT 3;