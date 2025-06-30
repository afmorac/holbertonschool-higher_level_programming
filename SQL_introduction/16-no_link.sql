-- Script para mostrar solo los que tengan nombre (no vacío y no NULL)
-- Muestra score y name, ordenado del mayor al menor
SELECT score, name FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
