-- Script para mostrar cuántas personas tienen el mismo score
-- Muestra el score y la cantidad de veces que aparece, ordenado por número
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
