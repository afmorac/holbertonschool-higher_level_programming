-- Script para crear la tabla first_table si no existe
-- Tiene dos columnas: id (entero) y name (texto de hasta 256)
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
