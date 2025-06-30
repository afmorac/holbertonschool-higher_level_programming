-- Script para mostrar las ciudades que pertenecen al estado de California
-- Usa subconsulta en vez de JOIN, y ordena por el ID de la ciudad

SELECT id, name FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;
