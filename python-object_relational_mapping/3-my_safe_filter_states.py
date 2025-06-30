#!/usr/bin/python3
"""
Script seguro contra SQL Injection.
Busca un estado en la base de datos usando parámetros seguros (%s)
"""

import MySQLdb
import sys

if __name__ == "__main__":
    usuario = sys.argv[1]
    clave = sys.argv[2]
    base = sys.argv[3]
    nombre_estado = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=usuario,
        passwd=clave,
        db=base
    )

    cur = db.cursor()

    # Evita SQL Injection usando parámetros
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (nombre_estado,))

    for fila in cur.fetchall():
        print(fila)

    cur.close()
    db.close()
