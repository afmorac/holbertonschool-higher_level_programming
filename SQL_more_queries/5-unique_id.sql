-- Script para crear la tabla unique_id con id único y valor por defecto 1
-- Si ya existe, no da error

CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
