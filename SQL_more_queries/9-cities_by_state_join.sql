-- Script para mostrar todas las ciudades junto al nombre de su estado
-- Usa JOIN y ordena por id de la ciudad

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
