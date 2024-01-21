-- Script that list al the cities of california 
SELECT cities.id, cities.name FROM cities, states WHERE cities.state_id = states.id AND states.name = 'california' ORDER BY cities.id ASC; 
