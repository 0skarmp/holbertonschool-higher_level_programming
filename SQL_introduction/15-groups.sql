-- SCRIPT THAT LISTS OF THE NUMBERS.
SELECT score, Count(*) as number FROM second_table GROUP BY score ORDER BY score DESC;
