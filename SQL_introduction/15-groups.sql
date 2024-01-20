-- Script to lists the numbere of recrords with the same score in the table

SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC; 