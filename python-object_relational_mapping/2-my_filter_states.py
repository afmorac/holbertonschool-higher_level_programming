#!/usr/bin/python3
"""
Script que muestra todos los estados que coinciden con el nombre ingresado.
Usa MySQLdb y construye la query con .format()
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Leer argumentos
    usuario = sys.argv[1]
    clave = sys.argv[2]
    base = sys.argv[3]
    nombre_estado = sys.argv[4]

    # Conexión a MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=usuario,
        passwd=clave,
        db=base
    )
    cur = db.cursor()

    # Construcción insegura con .format() (según lo pide el task)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(nombre_estado)

    cur.execute(query)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
