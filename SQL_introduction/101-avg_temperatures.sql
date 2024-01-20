-- SCRIPT 

SELECT city, AVG(value) as avg_temp FROM temparatures GROUPBY CITY ORDER BY avg_temp DESC;