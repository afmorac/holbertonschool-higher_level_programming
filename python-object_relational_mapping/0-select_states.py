#!/usr/bin/python3
"""
Script que se conecta a la base de datos y muestra todos los estados ordenados por id.
Usa MySQLdb y recibe argumentos desde la línea de comandos.
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
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Mostrar los resultados como tuplas
    for row in cur.fetchall():
        print(row)

    # Cerrar conexión
    cur.close()
    db.close()
