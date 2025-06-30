-- Script para crear el usuario user_0d_1 con todos los privilegios
-- Si ya existe, no falla

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
