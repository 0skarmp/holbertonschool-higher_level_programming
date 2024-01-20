-- SCRIPT 

SELECT city, AVG(value) as avg_temp FROM temperatures GROUPBY CITY ORDER BY avg_temp DESC;