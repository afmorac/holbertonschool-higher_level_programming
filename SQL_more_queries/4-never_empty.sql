-- Script para crear la tabla id_not_null con id que por defecto vale 1
-- Si no se especifica id, usará el valor 1 automáticamente

CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
