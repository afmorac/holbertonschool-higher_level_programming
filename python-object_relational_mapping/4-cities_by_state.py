#!/usr/bin/python3
"""
Script que lista todas las ciudades junto con su estado
de la base de datos hbtn_0e_4_usa, usando un JOIN.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    usuario = sys.argv[1]
    clave = sys.argv[2]
    base = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=usuario,
        passwd=clave,
        db=base
    )

    cur = db.cursor()

    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    for fila in cur.fetchall():
        print(fila)

    cur.close()
    db.close()
