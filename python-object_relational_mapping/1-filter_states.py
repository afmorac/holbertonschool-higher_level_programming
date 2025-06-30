#!/usr/bin/python3
"""
Script que lista todos los estados que empiezan con 'N' desde la base de datos.
Usa MySQLdb y ordena por id.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Conectarse a la base de datos
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()

    # Ejecutar SELECT con filtro
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Imprimir resultados
    for row in cur.fetchall():
        print(row)

    # Cerrar conexión
    cur.close()
    db.close()
