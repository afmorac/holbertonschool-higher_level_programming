-- Script para crear la tabla force_name con name obligatorio
-- Si ya existe, no falla

CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
