-- Script para crear la base hbtn_0d_2 y el usuario user_0d_2
-- El usuario solo tiene permiso de lectura (SELECT)

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
