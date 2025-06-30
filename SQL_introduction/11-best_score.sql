-- Script para mostrar los que tengan score mayor o igual a 10
-- Solo enseña score y name, ordenado del mejor score hacia abajo
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
